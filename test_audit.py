from audit_engine import audit_model

sample_description = """
An AI system that uses facial recognition to verify student identity during online exams.
"""

result = audit_model(sample_description)
print(result)
