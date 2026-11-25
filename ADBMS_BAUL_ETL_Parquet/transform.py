import duckdb

duckdb.sql("""
    COPY (
        SELECT DISTINCT
            TRIM(session_id) as session_id,
            session_date,
            customer_id,
            store_id,
            TRIM(device_type) as device_type,
            TRIM(SPLIT_PART(browser_os, '|', 1)) as browser,
            TRIM(SPLIT_PART(browser_os, '|', 2)) as os,
            session_purchase_made,
            session_duration_minutes,
            session_pages_visited,
            COALESCE(
                session_quality_score, 
                AVG(session_quality_score) OVER()
            ) AS session_quality_score
        FROM 'bronze.parquet'
    )
    TO 'silver.parquet'
    (FORMAT PARQUET);
""")