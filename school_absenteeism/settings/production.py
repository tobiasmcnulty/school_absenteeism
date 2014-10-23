from school_absenteeism.settings.staging import *

# There should be only minor differences from staging

DATABASES['default']['NAME'] = 'school_absenteeism_production'
DATABASES['default']['USER'] = 'school_absenteeism_production'

EMAIL_SUBJECT_PREFIX = '[School_Absenteeism Prod] '

# Uncomment if using celery worker configuration
# BROKER_URL = 'amqp://school_absenteeism_production:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/school_absenteeism_production' % os.environ