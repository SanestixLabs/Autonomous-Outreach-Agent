from datetime import datetime

from pydantic import BaseModel

from memory_service.repository import MemoryRepository
from memory_service.schema import (
    CachedOutputs,
    InteractionHistory,
    LeadMemory,
    LeadState,
    WorkflowExecution,
    WorkflowStatus,
)


class MemoryService:
    """
    Business logic for managing lead memory.
    """

    def __init__(self, repository: MemoryRepository):
        self.repository = repository

    def create_lead(self, lead_id: str, company_name: str) -> LeadMemory:
        lead = LeadMemory(
            lead_id=lead_id,
            company_name=company_name,
        )

        self.repository.save(lead)
        return lead

    def get_lead(self, lead_id: str) -> LeadMemory | None:
        return self.repository.get(lead_id)

    def update_lead_state(
        self,
        lead_id: str,
        lead_state: LeadState,
    ) -> None:
        lead = self._get_existing_lead(lead_id)
        lead.lead_state = lead_state
        self.repository.save(lead)

    def record_interaction(
        self,
        lead_id: str,
        reply_received: bool = False,
        meeting_booked: bool = False,
    ) -> None:
        lead = self._get_existing_lead(lead_id)

        lead.interaction_history.last_contacted_at = datetime.utcnow()
        lead.interaction_history.reply_received = reply_received
        lead.interaction_history.meeting_booked = meeting_booked

        if not meeting_booked:
            lead.interaction_history.follow_up_count += 1

        self.repository.save(lead)

    def cache_output(
        self,
        lead_id: str,
        output_type: str,
        output: BaseModel,
    ) -> None:
        lead = self._get_existing_lead(lead_id)

        if not hasattr(lead.cached_outputs, output_type):
            raise ValueError(f"Unsupported output type: {output_type}")

        setattr(lead.cached_outputs, output_type, output)

        self.repository.save(lead)

    def record_workflow(
        self,
        lead_id: str,
        workflow_name: str,
        status: WorkflowStatus,
    ) -> None:
        lead = self._get_existing_lead(lead_id)

        lead.workflow_history.append(
            WorkflowExecution(
                workflow_name=workflow_name,
                status=status,
            )
        )

        lead.last_workflow = workflow_name

        self.repository.save(lead)

    def delete_lead(self, lead_id: str) -> None:
        self.repository.delete(lead_id)

    def _get_existing_lead(self, lead_id: str) -> LeadMemory:
        lead = self.repository.get(lead_id)

        if lead is None:
            raise ValueError(f"Lead '{lead_id}' not found.")

        return lead