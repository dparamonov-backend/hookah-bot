def validate_phone(phone: str) -> bool:
    """Проверяет наличие 10 цифр в номере"""
    cleaned = (
        phone.replace("+",'').replace("-",'').replace(" ", '').replace('(','').replace(')',''))
    return cleaned.isdigit() and len(cleaned) >= 10
