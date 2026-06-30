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
    
## Devices & Network Identifiers Table
- customer_id
- misdn
- imsi
- imei
- status
- activated_at
- terminated_at