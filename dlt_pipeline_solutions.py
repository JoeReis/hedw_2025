import sys
import dlt
from dlt.sources.sql_database import sql_database

def load_university_pipeline():
    source = sql_database().with_resources(
        "courses",
        "course_assignments",
        "enrollments",
        "professors",
        "students",
        "student_admissions"
    )
    
    pipeline = dlt.pipeline(
        pipeline_name="university_data",
        destination="duckdb",
        dataset_name="staging",
    )
    
    load_info = pipeline.run(source)
    print(load_info)

if __name__ == "__main__":
    load_university_pipeline()