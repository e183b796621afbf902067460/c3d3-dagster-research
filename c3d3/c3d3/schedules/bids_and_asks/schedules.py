from dagster import ScheduleDefinition

from c3d3.jobs.bids_and_asks.jobs import dag


every_15th_minute = ScheduleDefinition(
    name='bids_and_asks',
    job=dag,
    cron_schedule="*/15 * * * *"
)
