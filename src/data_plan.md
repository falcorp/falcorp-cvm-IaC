# Data Plan for CVM

This is a plan for the creation of fictious data for cvm solution. The data will be grouped into the following categories:

1. customer
2. cdr data
3. product data
4. recharge event data

## Customer Data
- Demographics
    - Customer_ID
    - Registration_Date
    - Termination_Date
    - DOB
    - gender
    - region
    - signup channel
- Acquisition & Channel Context
    - Signup_channel
    - Signup_promo_code
    - Ported_in_status
    - previous_carrier
- Contract Status
    - Plan_ID
    - BYOD
    - Registration_device_tac
    - Payment_method
    
### Devices & Network Identifiers Table
- customer_id
- misdn
- imsi
- imei
- status
- activated_at
- terminated_at

## Product Data# Data Plan for CVM

This is a plan for the creation of fictious data for cvm solution. The data will be grouped into the following categories:

1. customer
2. cdr data
3. product data
4. recharge event data

## Customer Data
- Demographics
    - Customer_ID
    - Registration_Date
    - Termination_Date
    - DOB
    - gender
    - region
    - signup channel
- Acquisition & Channel Context
    - Signup_channel
    - Signup_promo_code
    - Ported_in_status
    - previous_carrier
- Contract Status
    - Plan_ID
    - BYOD
    - Registration_device_tac
    - Payment_method
    
## Devices & Network Identifiers Table
This table stores the mapping between the customer, their mobile phone number (MSISDN), and their physical SIM card (IMSI), preserving a history of device and network swaps.

| Column Name | Data Type | Key / Constraint | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| **assignment_id** | VARCHAR (50) | **PK** | Unique identifier for this specific card/network subscription pairing. | `ASN-902143` |
| **customer_id** | VARCHAR (50) | **FK** | Foreign Key linking back to the `customer_master` table. | `CUST-2026-89432` |
| **msisdn** | VARCHAR (15) | Unique, Not Null | The subscriber's mobile phone number (including country code). | `14155552671` |
| **imsi** | VARCHAR (15) | Unique, Not Null | International Mobile Subscriber Identity hardcoded onto the physical or eSIM. | `310410000000001` |
| **imei** | VARCHAR (15) | Nullable | The unique hardware identifier of the physical phone handset. | `351944112345678` |
| **status** | VARCHAR (15) | Check, Default 'ACTIVE'| The life-cycle state of the SIM/number pair (`ACTIVE`, `SUSPENDED`, `REPLACED`). | `ACTIVE` |
| **activated_at** | TIMESTAMP | Not Null, Default Current| Exact timestamp when this specific network alignment went live. | `2026-06-25 12:23:21` |


## Product Data
This table serves as the master catalog for all available plans, add-ons, and passes within the MVNO ecosystem.

| Column Name | Data Type | Key / Constraint | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| **product_id** | VARCHAR (50) | **PK** | Unique identifier for the product SKU. | `PLAN-UNLTD-GENZ` |
| **product_name** | VARCHAR (100) | Not Null | User-facing name of the plan or package. | `Gen Z Unlimited Data Plan` |
| **product_type** | VARCHAR (20) | Check | Categorizes the product (`BASE_PLAN`, `DATA_ADDON`, `ROAMING_PASS`, `VOICE_ADDON`, `SMS_ADDON`). | `BASE_PLAN` |
| **billing_type** | VARCHAR (15) | Check | Determines payment style (`PREPAID`, `POSTPAID`). | `PREPAID` |
| **price** | DECIMAL (10,2) | Not Null, >= 0.00 | The retail cost of the product before taxes. | `29.99` |
| **currency** | VARCHAR (3) | Default 'USD' | Standard 3-letter currency code. | `USD` |
| **validity_days** | INT | Not Null, > 0 | Lifecycle of the product before expiration/renewal. | `30` |
| **data_gb_allowance**| DECIMAL (6,2) | Default -1.00 | Included data bucket in GB. `-1.00` denotes Unlimited. | `25.00` |
| **voice_minutes** | INT | Default -1 | Included national voice minutes. `-1` denotes Unlimited. | `500` |
| **sms_count** | INT | Default -1 | Included text messages. `-1` denotes Unlimited. | `1000` |
| **throttled_after_limit**| BOOLEAN | Default False | If True, data speeds drop instead of cutting off or overcharging. | `True` |
| **is_active** | BOOLEAN | Default True | Flag to toggle visibility in the customer portal/app. | `True` |
| **created_at** | TIMESTAMP | Default Current | Audit timestamp for record creation. | `2026-06-30 12:00:00` |
| **updated_at** | TIMESTAMP | Default Current | Audit timestamp for record modification. | `2026-06-30 12:00:00` |