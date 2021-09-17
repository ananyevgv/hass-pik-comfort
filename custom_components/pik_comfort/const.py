"""Constants for energosbyt_plus integration"""
from typing import Final

DOMAIN: Final = "pik_comfort"

ATTRIBUTION: Final = "Данные получены от ПИК Комфорт"

ATTR_ACCOUNT_CODE: Final = "account_code"
ATTR_ACCOUNT_ID: Final = "account_id"
ATTR_ADDRESS: Final = "address"
ATTR_AMOUNT: Final = "amount"
ATTR_BENEFITS: Final = "benefits"
ATTR_CALL_PARAMS: Final = "call_params"
ATTR_CHARGED: Final = "charged"
ATTR_CLEAR: Final = "clear"
ATTR_COMMENT: Final = "comment"
ATTR_CORRECT: Final = "correct"
ATTR_COST: Final = "cost"
ATTR_DESCRIPTION: Final = "description"
ATTR_DETAILS: Final = "details"
ATTR_END: Final = "end"
ATTR_FULL_NAME: Final = "full_name"
ATTR_IGNORE_READINGS: Final = "ignore_readings"
ATTR_IGNORE_PERIOD: Final = "ignore_period"
ATTR_INCREMENTAL: Final = "incremental"
ATTR_READINGS: Final = "readings"
ATTR_INITIAL: Final = "initial"
ATTR_INSTALL_DATE: Final = "install_date"
ATTR_INSURANCE: Final = "insurance"
ATTR_INVOICE_ID: Final = "invoice_id"
ATTR_LAST_INDICATIONS_DATE: Final = "last_indications_date"
ATTR_LAST_SUBMITTED: Final = "last_submitted"
ATTR_LIVING_AREA: Final = "living_area"
ATTR_METER_CATEGORY: Final = "meter_category"
ATTR_METER_CODE: Final = "meter_code"
ATTR_METER_MODEL: Final = "meter_model"
ATTR_MODEL: Final = "model"
ATTR_NOTIFICATION: Final = "notification"
ATTR_PAID: Final = "paid"
ATTR_PAID_AT: Final = "paid_at"
ATTR_PENALTY: Final = "penalty"
ATTR_PERIOD: Final = "period"
ATTR_PREVIOUS: Final = "previous"
ATTR_REASON: Final = "reason"
ATTR_RECALCULATIONS: Final = "recalculations"
ATTR_REMAINING_DAYS: Final = "remaining_days"
ATTR_RESULT: Final = "result"
ATTR_SERVICE_NAME: Final = "service_name"
ATTR_SERVICE_TYPE: Final = "service_type"
ATTR_START: Final = "start"
ATTR_STATUS: Final = "status"
ATTR_SUBMIT_PERIOD_ACTIVE: Final = "submit_period_active"
ATTR_SUBMIT_PERIOD_END: Final = "submit_period_end"
ATTR_SUBMIT_PERIOD_START: Final = "submit_period_start"
ATTR_SUCCESS: Final = "success"
ATTR_TOTAL: Final = "total"
ATTR_TOTAL_AREA: Final = "total_area"
ATTR_UNIT: Final = "unit"
ATTR_MANUFACTURER: Final = "manufacturer"
ATTR_BRAND: Final = "brand"
ATTR_TYPE: Final = "type"
ATTR_ACCEPTED: Final = "accepted"
ATTR_SUBMITTED: Final = "submitted"
ATTR_CURRENT: Final = "current"
ATTR_LAST_CHECKUP_DATE: Final = "last_checkup_date"
ATTR_NEXT_CHECKUP_DATE: Final = "next_checkup_date"
ATTR_ACCURACY: Final = "accuracy"
ATTR_DIGITS: Final = "digits"
ATTR_ZONES: Final = "zones"
ATTR_INCREASE_RATIO: Final = "increase_ratio"
ATTR_INCREASE_AMOUNT: Final = "increase_amount"

CONF_ACCOUNTS: Final = "accounts"
CONF_DEV_PRESENTATION: Final = "dev_presentation"
CONF_CHARGES: Final = "charges"
CONF_SERVICE_CHARGES: Final = "service_charges"
CONF_LAST_PAYMENT: Final = "last_payment"
CONF_METERS: Final = "meters"
CONF_NAME_FORMAT: Final = "name_format"
CONF_USER_AGENT: Final = "user_agent"

DATA_API_OBJECTS: Final = DOMAIN + "_api_objects"
DATA_ENTITIES: Final = DOMAIN + "_entities"
DATA_FINAL_CONFIG: Final = DOMAIN + "_final_config"
DATA_UPDATE_ROUTINES: Final = DOMAIN + "_update_routines"
DATA_UPDATE_LISTENERS: Final = DOMAIN + "_update_listeners"
DATA_YAML_CONFIG: Final = DOMAIN + "_yaml_config"

DEFAULT_NAME_FORMAT_EN_ACCOUNTS: Final = "{account_code_short} {type_en_cap}"
DEFAULT_NAME_FORMAT_EN_METERS: Final = "{account_code_short} {type_en_cap} {code}"
DEFAULT_NAME_FORMAT_EN_CHARGES: Final = "{account_code_short} {type_en_cap}"
DEFAULT_NAME_FORMAT_EN_LAST_PAYMENT: Final = "{account_code_short} {type_en_cap}"
DEFAULT_NAME_FORMAT_EN_SERVICE_CHARGES: Final = (
    "{account_code_short} {type_en_cap} - {service_name}"
)

DEFAULT_NAME_FORMAT_RU_ACCOUNTS: Final = "{account_code_short} {type_ru_cap}"
DEFAULT_NAME_FORMAT_RU_METERS: Final = "{account_code_short} {type_ru_cap} {code}"
DEFAULT_NAME_FORMAT_RU_CHARGES: Final = "{account_code_short} {type_ru_cap}"
DEFAULT_NAME_FORMAT_RU_LAST_PAYMENT: Final = "{account_code_short} {type_ru_cap}"
DEFAULT_NAME_FORMAT_RU_SERVICE_CHARGES: Final = (
    "{account_code_short} {type_ru_cap} - {service_name}"
)

DEFAULT_MAX_INDICATIONS: Final = 3
DEFAULT_SCAN_INTERVAL: Final = 60 * 60 * 24  # 24 hours

SUPPORTED_PLATFORMS: Final = ("sensor", "binary_sensor")

FORMAT_VAR_ACCOUNT_CODE: Final = "account_code"
FORMAT_VAR_ACCOUNT_CODE_SHORT: Final = "account_code_short"
FORMAT_VAR_ACCOUNT_ID: Final = "account_id"
FORMAT_VAR_CODE: Final = "code"
FORMAT_VAR_ID: Final = "id"
FORMAT_VAR_PROVIDER_CODE: Final = "provider_code"
FORMAT_VAR_PROVIDER_NAME: Final = "provider_name"
FORMAT_VAR_TYPE_EN: Final = "type_en"
FORMAT_VAR_TYPE_RU: Final = "type_ru"
ATTR_SERVICES: Final = "services"
CONF_BRANCH: Final = "branch"
DATA_PLATFORM_ENTITY_REGISTRARS: Final = DOMAIN + "_platform_entity_registrars"