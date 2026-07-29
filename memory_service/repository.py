from memory_service.schema import LeadMemory


class MemoryRepository:
    """
    In-memory repository for storing lead memory.
    Can be replaced with a database implementation later.
    """

    def __init__(self):
        self._memory: dict[str, LeadMemory] = {}

    def save(self, lead_memory: LeadMemory) -> None:
        """
        Save or update a lead.
        """
        self._memory[lead_memory.lead_id] = lead_memory

    def get(self, lead_id: str) -> LeadMemory | None:
        """
        Retrieve a lead by its ID.
        """
        return self._memory.get(lead_id)

    def delete(self, lead_id: str) -> None:
        """
        Remove a lead from memory.
        """
        self._memory.pop(lead_id, None)

    def exists(self, lead_id: str) -> bool:
        """
        Check if a lead exists.
        """
        return lead_id in self._memory

    def list_all(self) -> list[LeadMemory]:
        """
        Return all stored leads.
        """
        return list(self._memory.values())