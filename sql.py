import sqlite3


conn = sqlite3.connect('health_db.sqlite3')
curs = conn.cursor()

query_total_n_patients = """
select count(*)
from patients;
"""

query_jaundice_symptoms = """
select symptoms
from ailments
where disease = 'Jaundice';
"""

query_difference_diabetes_arthritis = """
Select
(SELECT COUNT(*) FROM patient_ailment WHERE patient_ailment='Diabetes')
- (SELECT COUNT(*) FROM patient_ailment WHERE patient_ailment='Arthritis');
"""

query_most_frequent_ailment = """
Select patient_ailment, count(patient_ailment)
FROM patient_ailment
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
"""

query_names_with_diabetes = """
SELECT p.name
FROM patients p, patient_ailment pa
WHERE p.patient_id=pa.patient_id AND pa.patient_ailment='Diabetes';
"""

if __name__ == '__main__':
    queries = {k: v for k, v in locals().items() if k.startswith('query')}

    for q in queries:
        print(f'{q}: {curs.execute(queries[q]).fetchall()}')
        print('-----------------------------------')


conn.close()
