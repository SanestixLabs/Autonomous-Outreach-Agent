from enum import Enum


class WorkflowType(str, Enum):
    COMPANY_ANALYSIS = "Company Analysis"
    LEAD_QUALIFICATION = "Lead Qualification"
    SERVICE_RECOMMENDATION = "Service Recommendation"
    PERSONALIZED_EMAIL = "Personalized Email"
    CRM_SYNC = "CRM Sync"