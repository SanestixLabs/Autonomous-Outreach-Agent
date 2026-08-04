from common.enums import WorkflowType

from workflow_router.schema import (
    PipelineStage,
    RouteContext,
    RoutingDecision,
)


PIPELINE_ROUTES = {
    PipelineStage.INITIAL: WorkflowType.COMPANY_ANALYSIS,
    PipelineStage.COMPANY_ANALYZED: WorkflowType.LEAD_QUALIFICATION,
    PipelineStage.LEAD_QUALIFIED: WorkflowType.SERVICE_RECOMMENDATION,
    PipelineStage.SERVICE_RECOMMENDED: WorkflowType.PERSONALIZED_EMAIL,
}


class WorkflowRouter:

    def route(self, context: RouteContext) -> RoutingDecision:

        # Existing lead
        if context.follow_up_decision is not None:
            return RoutingDecision(
                next_workflow=context.follow_up_decision.recommended_workflow,
                reason=context.follow_up_decision.reason,
            )

        # New lead
        workflow = PIPELINE_ROUTES.get(context.pipeline_stage)

        if workflow is None:
            return RoutingDecision(
                next_workflow=None,
                reason="Pipeline completed.",
            )

        return RoutingDecision(
            next_workflow=workflow,
            reason=f"Routing from {context.pipeline_stage.value}.",
        )