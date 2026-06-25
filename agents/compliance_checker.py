from tools.banking_tools import verify_kyc

def compliance_agent(customer_id):
    return verify_kyc(customer_id)
