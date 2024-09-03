from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField # type: ignore
from django.core.validators import MaxValueValidator, MinValueValidator
# MultiSelectField: https://pypi.org/project/django-multiselectfield/

class Patient(models.Model):
    '''
    
    Page 2 of the Template

    '''

    # Demographic Data
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(null=True) # consider automating
    sex = models.CharField(null=True, max_length=6, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ])

    address = models.TextField(blank=True, null=True)

    parent_guardian_first_name = models.CharField(max_length=50, blank=True, null=True) 
    parent_guardian_last_name = models.CharField(max_length=50, blank=True, null=True)
    informant_first_name = models.CharField(max_length=50, blank=True, null=True)
    informant_last_name = models.CharField(max_length=50, blank=True, null=True)
    reliability = models.CharField(blank=True, null=True, max_length=9, choices=[
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    ])

    dwelling_type = models.CharField(blank=True, null=True, max_length=9, choices=[ 
        ('House', 'House'),
        ('Apartment', 'Apartment'),
    ])
    number_of_rooms = models.PositiveIntegerField(blank=True, null=True) 
    appliances = MultiSelectField(blank=True, null=True, choices=[ 
        ('Radio', 'Radio'),
        ('TV', 'TV'),
        ('Refrigerator', 'Refrigerator'),
    ])

    number_of_household_members = models.PositiveIntegerField(blank=True, null=True) 
    transportation = models.CharField(blank=True, null=True, max_length=10, choices=[ 
        ('None', 'None'),
        ('Car', 'Car'),
        ('Jeep', 'Jeep'),
        ('Motorcycle', 'Motorcycle'),
    ])

    landline_number = models.CharField(blank=True, null=True, max_length=11) # 11 digits to allow for overseas calls
    phone_number = models.CharField(blank=True, null=True, max_length=12) # use country code 63 instead of 0
    attending_physician_first_name = models.CharField(max_length=50, blank=True, null=True) 
    attending_physician_last_name = models.CharField(max_length=50, blank=True, null=True)

    nationality = models.CharField(blank=True, null=True, max_length=50, choices=[                             
        ('Afghan', 'Afghan'), # list taken from https://assets.publishing.service.gov.uk/media/5a81f5fce5274a2e87dc068d/CH_Nationality_List_20171130_v1.csv
        ('Albanian', 'Albanian'),
        ('Algerian', 'Algerian'),
        ('American', 'American'),
        ('Andorran', 'Andorran'),
        ('Angolan', 'Angolan'),
        ('Anguillan', 'Anguillan'),
        ('Argentine', 'Argentine'),
        ('Armenian', 'Armenian'),
        ('Australian', 'Australian'),
        ('Austrian', 'Austrian'),
        ('Azerbaijani', 'Azerbaijani'),
        ('Bahamian', 'Bahamian'),
        ('Bahraini', 'Bahraini'),
        ('Bangladeshi', 'Bangladeshi'),
        ('Barbadian', 'Barbadian'),
        ('Belarusian', 'Belarusian'),
        ('Belgian', 'Belgian'),
        ('Belizean', 'Belizean'),
        ('Beninese', 'Beninese'),
        ('Bermudian', 'Bermudian'),
        ('Bhutanese', 'Bhutanese'),
        ('Bolivian', 'Bolivian'),
        ('Botswanan', 'Botswanan'),
        ('Brazilian', 'Brazilian'),
        ('British', 'British'),
        ('British Virgin Islander', 'British Virgin Islander'),
        ('Bruneian', 'Bruneian'),
        ('Bulgarian', 'Bulgarian'),
        ('Burkinan', 'Burkinan'),
        ('Burmese', 'Burmese'),
        ('Burundian', 'Burundian'),
        ('Cambodian', 'Cambodian'),
        ('Cameroonian', 'Cameroonian'),
        ('Canadian', 'Canadian'),
        ('Cape Verdean', 'Cape Verdean'),
        ('Cayman Islander', 'Cayman Islander'),
        ('Central African', 'Central African'),
        ('Chadian', 'Chadian'),
        ('Chilean', 'Chilean'),
        ('Chinese', 'Chinese'),
        ('Citizen of Antigua and Barbuda', 'Citizen of Antigua and Barbuda'),
        ('Citizen of Bosnia and Herzegovina', 'Citizen of Bosnia and Herzegovina'),
        ('Citizen of Guinea-Bissau', 'Citizen of Guinea-Bissau'),
        ('Citizen of Kiribati', 'Citizen of Kiribati'),
        ('Citizen of Seychelles', 'Citizen of Seychelles'),
        ('Citizen of the Dominican Republic', 'Citizen of the Dominican Republic'),
        ('Citizen of Vanuatu ', 'Citizen of Vanuatu '),
        ('Colombian', 'Colombian'),
        ('Comoran', 'Comoran'),
        ('Congolese (Congo)', 'Congolese (Congo)'),
        ('Congolese (DRC)', 'Congolese (DRC)'),
        ('Cook Islander', 'Cook Islander'),
        ('Costa Rican', 'Costa Rican'),
        ('Croatian', 'Croatian'),
        ('Cuban', 'Cuban'),
        ('Cymraes', 'Cymraes'),
        ('Cymro', 'Cymro'),
        ('Cypriot', 'Cypriot'),
        ('Czech', 'Czech'),
        ('Danish', 'Danish'),
        ('Djiboutian', 'Djiboutian'),
        ('Dominican', 'Dominican'),
        ('Dutch', 'Dutch'),
        ('East Timorese', 'East Timorese'),
        ('Ecuadorean', 'Ecuadorean'),
        ('Egyptian', 'Egyptian'),
        ('Emirati', 'Emirati'),
        ('English', 'English'),
        ('Equatorial Guinean', 'Equatorial Guinean'),
        ('Eritrean', 'Eritrean'),
        ('Estonian', 'Estonian'),
        ('Ethiopian', 'Ethiopian'),
        ('Faroese', 'Faroese'),
        ('Fijian', 'Fijian'),
        ('Filipino', 'Filipino'),
        ('Finnish', 'Finnish'),
        ('French', 'French'),
        ('Gabonese', 'Gabonese'),
        ('Gambian', 'Gambian'),
        ('Georgian', 'Georgian'),
        ('German', 'German'),
        ('Ghanaian', 'Ghanaian'),
        ('Gibraltarian', 'Gibraltarian'),
        ('Greek', 'Greek'),
        ('Greenlandic', 'Greenlandic'),
        ('Grenadian', 'Grenadian'),
        ('Guamanian', 'Guamanian'),
        ('Guatemalan', 'Guatemalan'),
        ('Guinean', 'Guinean'),
        ('Guyanese', 'Guyanese'),
        ('Haitian', 'Haitian'),
        ('Honduran', 'Honduran'),
        ('Hong Konger', 'Hong Konger'),
        ('Hungarian', 'Hungarian'),
        ('Icelandic', 'Icelandic'),
        ('Indian', 'Indian'),
        ('Indonesian', 'Indonesian'),
        ('Iranian', 'Iranian'),
        ('Iraqi', 'Iraqi'),
        ('Irish', 'Irish'),
        ('Israeli', 'Israeli'),
        ('Italian', 'Italian'),
        ('Ivorian', 'Ivorian'),
        ('Jamaican', 'Jamaican'),
        ('Japanese', 'Japanese'),
        ('Jordanian', 'Jordanian'),
        ('Kazakh', 'Kazakh'),
        ('Kenyan', 'Kenyan'),
        ('Kittitian', 'Kittitian'),
        ('Kosovan', 'Kosovan'),
        ('Kuwaiti', 'Kuwaiti'),
        ('Kyrgyz', 'Kyrgyz'),
        ('Lao', 'Lao'),
        ('Latvian', 'Latvian'),
        ('Lebanese', 'Lebanese'),
        ('Liberian', 'Liberian'),
        ('Libyan', 'Libyan'),
        ('Liechtenstein citizen', 'Liechtenstein citizen'),
        ('Lithuanian', 'Lithuanian'),
        ('Luxembourger', 'Luxembourger'),
        ('Macanese', 'Macanese'),
        ('Macedonian', 'Macedonian'),
        ('Malagasy', 'Malagasy'),
        ('Malawian', 'Malawian'),
        ('Malaysian', 'Malaysian'),
        ('Maldivian', 'Maldivian'),
        ('Malian', 'Malian'),
        ('Maltese', 'Maltese'),
        ('Marshallese', 'Marshallese'),
        ('Martiniquais', 'Martiniquais'),
        ('Mauritanian', 'Mauritanian'),
        ('Mauritian', 'Mauritian'),
        ('Mexican', 'Mexican'),
        ('Micronesian', 'Micronesian'),
        ('Moldovan', 'Moldovan'),
        ('Monegasque', 'Monegasque'),
        ('Mongolian', 'Mongolian'),
        ('Montenegrin', 'Montenegrin'),
        ('Montserratian', 'Montserratian'),
        ('Moroccan', 'Moroccan'),
        ('Mosotho', 'Mosotho'),
        ('Mozambican', 'Mozambican'),
        ('Namibian', 'Namibian'),
        ('Nauruan', 'Nauruan'),
        ('Nepalese', 'Nepalese'),
        ('New Zealander', 'New Zealander'),
        ('Nicaraguan', 'Nicaraguan'),
        ('Nigerian', 'Nigerian'),
        ('Nigerien', 'Nigerien'),
        ('Niuean', 'Niuean'),
        ('North Korean', 'North Korean'),
        ('Northern Irish', 'Northern Irish'),
        ('Norwegian', 'Norwegian'),
        ('Omani', 'Omani'),
        ('Pakistani', 'Pakistani'),
        ('Palauan', 'Palauan'),
        ('Palestinian', 'Palestinian'),
        ('Panamanian', 'Panamanian'),
        ('Papua New Guinean', 'Papua New Guinean'),
        ('Paraguayan', 'Paraguayan'),
        ('Peruvian', 'Peruvian'),
        ('Pitcairn Islander', 'Pitcairn Islander'),
        ('Polish', 'Polish'),
        ('Portuguese', 'Portuguese'),
        ('Prydeinig', 'Prydeinig'),
        ('Puerto Rican', 'Puerto Rican'),
        ('Qatari', 'Qatari'),
        ('Romanian', 'Romanian'),
        ('Russian', 'Russian'),
        ('Rwandan', 'Rwandan'),
        ('Salvadorean', 'Salvadorean'),
        ('Sammarinese', 'Sammarinese'),
        ('Samoan', 'Samoan'),
        ('Sao Tomean', 'Sao Tomean'),
        ('Saudi Arabian', 'Saudi Arabian'),
        ('Scottish', 'Scottish'),
        ('Senegalese', 'Senegalese'),
        ('Serbian', 'Serbian'),
        ('Sierra Leonean', 'Sierra Leonean'),
        ('Singaporean', 'Singaporean'),
        ('Slovak', 'Slovak'),
        ('Slovenian', 'Slovenian'),
        ('Solomon Islander', 'Solomon Islander'),
        ('Somali', 'Somali'),
        ('South African', 'South African'),
        ('South Korean', 'South Korean'),
        ('South Sudanese', 'South Sudanese'),
        ('Spanish', 'Spanish'),
        ('Sri Lankan', 'Sri Lankan'),
        ('St Helenian', 'St Helenian'),
        ('St Lucian', 'St Lucian'),
        ('Stateless', 'Stateless'),
        ('Sudanese', 'Sudanese'),
        ('Surinamese', 'Surinamese'),
        ('Swazi', 'Swazi'),
        ('Swedish', 'Swedish'),
        ('Swiss', 'Swiss'),
        ('Syrian', 'Syrian'),
        ('Taiwanese', 'Taiwanese'),
        ('Tajik', 'Tajik'),
        ('Tanzanian', 'Tanzanian'),
        ('Thai', 'Thai'),
        ('Togolese', 'Togolese'),
        ('Tongan', 'Tongan'),
        ('Trinidadian', 'Trinidadian'),
        ('Tristanian', 'Tristanian'),
        ('Tunisian', 'Tunisian'),
        ('Turkish', 'Turkish'),
        ('Turkmen', 'Turkmen'),
        ('Turks and Caicos Islander', 'Turks and Caicos Islander'),
        ('Tuvaluan', 'Tuvaluan'),
        ('Ugandan', 'Ugandan'),
        ('Ukrainian', 'Ukrainian'),
        ('Uruguayan', 'Uruguayan'),
        ('Uzbek', 'Uzbek'),
        ('Vatican citizen', 'Vatican citizen'),
        ('Venezuelan', 'Venezuelan'),
        ('Vietnamese', 'Vietnamese'),
        ('Vincentian', 'Vincentian'),
        ('Wallisian', 'Wallisian'),
        ('Welsh', 'Welsh'),
        ('Yemeni', 'Yemeni'),
        ('Zambian', 'Zambian'),
        ('Zimbabwean', 'Zimbabwean'),
    ])
    religion = models.CharField(blank=True, null=True, max_length=17, choices=[
        ('Roman Catholic', 'Roman Catholic'),
        ('Protestant', 'Protestant'),
        ('Muslim', 'Muslim'),
        ('Iglesia ni Cristo', 'Iglesia ni Cristo'),
        ('Aglipay', 'Aglipay'),
        ('Other', 'Other'),
    ])

    annual_family_income = models.CharField(blank=True, null=True, max_length=11, choices=[
        ('< 50k', '< 50k'),
        ('50k - 100k', '50k - 100k'),
        ('100k - 200k', '100k - 200k'),
        ('200k - 300k', '200k - 300k'),
        ('> 300k', '> 300k'),
    ])

    # History
    chief_complaint = models.CharField(max_length=50, blank=True, null=True)
    concerns_regarding_problem = models.TextField(blank=True, null=True)
    history_of_present_illness = models.TextField(blank=True, null=True)
    
    # Context
    # Stakeholder Analysis
    stakeholder = models.CharField(max_length=50, blank=True, null=True)
    interest_in_issue = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    level_of_influence = models.TextField(blank=True, null=True)
    
    pertinent_beliefs = models.TextField(blank=True, null=True)

    impact_on_family = models.TextField(blank=True, null=True)
    
    # Community Factors
    facilitating_community_factors = models.TextField(blank=True, null=True)
    hindering_community_factors = models.TextField(blank=True, null=True)
    burden_of_illness_community_factors = models.TextField(blank=True, null=True)
    pertinent_legislation_or_policies_community_factors = models.TextField(blank=True, null=True)

    # Nutritional History
    breastfed_till = models.CharField(max_length=50, blank=True, null=True) #is this in years? months?
    formula = models.CharField(max_length=50, blank=True, null=True)
    weaning_age = models.PositiveIntegerField(blank=True, null=True)
    current_diet = models.CharField(max_length=50, blank=True, null=True)
    food_allergy = models.CharField(max_length=50, blank=True, null=True)

    # Birth Maternal
    term = models.CharField(max_length=50, blank=True, null=True)
    delivered_via = models.CharField(max_length=50, blank=True, null=True)
    to_a = models.PositiveIntegerField(help_text="year old",blank=True, null=True)
    g_mother = models.PositiveIntegerField(blank=True, null=True)
    p_mother = models.PositiveIntegerField(blank=True, null=True)
    bw = models.FloatField(blank=True, null=True)
    attended_by_first_name = models.CharField(max_length=50, blank=True, null=True) 
    attended_by_last_name = models.CharField(max_length=50, blank=True, null=True)
    perinatal_cx = models.CharField(max_length=50, blank=True, null=True) 

    # Developmental Milestones
    gross_motor_developmental_milestones = models.TextField(blank=True, null=True)
    adaptive_fine_motor_developmental_milestones = models.TextField(blank=True, null=True)
    language_developmental_milestones = models.TextField(blank=True, null=True)
    personal_and_social_developmental_milestones = models.TextField(blank=True, null=True)

    # Review of Systems
    general_symptoms = MultiSelectField(blank=True, null=True, choices=[
        ('Fever', 'Fever'),
        ('Weight Gain', 'Weight Gain'),
        ('Weight Loss', 'Weight Loss'),
        ('Weakness', 'Weakness'),
        ('Fatigue', 'Fatigue'),
    ])
    other_general_symptoms = models.CharField(max_length=50, blank=True, null=True)
    musculoskeletal_or_dermatologic = MultiSelectField(blank=True, null=True, choices=[
        ('Rashes', 'Rashes'),
        ('Lumps', 'Lumps'),
        ('Sores', 'Sores'),
        ('Itching', 'Itching'),
        ('Muscle Pains', 'Muscle Pains'),
        ('Joint Pains', 'Joint Pains'),
        ('Changes in Color', 'Changes in Color'),
        ('Joint Swelling', 'Joint Swelling'),
        ('Changes in hair/nails', 'Changes in hair/nails'),
        ('Gout', 'Gout'),
    ])
    heent = MultiSelectField(blank=True, null=True, choices=[
        ('Headache', 'Headache'),
        ('Dizziness', 'Dizziness'),
        ('Blurring of Vision', 'Blurring of Vision'),
        ('Tinnitus', 'Tinnitus'),
        ('Deafness', 'Deafness'),
        ('Nosebleeds', 'Nosebleeds'),
        ('Frequent Colds', 'Frequent Colds'),
        ('Hoarseness', 'Hoarseness'),
        ('Dry Mouth', 'Dry Mouth'),
        ('Gum Bleeding', 'Gum Bleeding'),
        ('Enlarged LN', 'Enlarged LN'),
    ])
    respiratory = MultiSelectField(blank=True, null=True, choices=[
        ('Dyspnea', 'Dyspnea'),
        ('Hemoptysis', 'Hemoptysis'),
        ('Cough', 'Cough'),
        ('Wheezing', 'Wheezing'),
    ])
    cardiovascular = MultiSelectField(blank=True, null=True, choices=[
        ('Palpitations', 'Palpitations'),
        ('Chest Pains', 'Chest Pains'),
        ('Syncope', 'Syncope'),
        ('Orthopnea', 'Orthopnea'),
    ])
    other_cardiovascular_symptoms = models.CharField(max_length=50, blank=True, null=True)
    gastrointestinal = MultiSelectField(blank=True, null=True, choices=[
        ('Nausea', 'Nausea'),
        ('Vomiting', 'Vomiting'),
        ('Dysphagia', 'Dysphagia'),
        ('Heartburn', 'Heartburn'),
        ('Change in Bowel Habits', 'Change in Bowel Habits'),
        ('Rectal Bleeding', 'Rectal Bleeding'),
        ('Jaundice', 'Jaundice'),
    ])
    genitourinary = MultiSelectField(blank=True, null=True, choices=[
        ('Nocturia', 'Nocturia'),
        ('Dysuria', 'Dysuria'),
        ('Frequency', 'Frequency'),
        ('Hematuria', 'Hematuria'),
    ])
    other_genitourinary_symptoms = models.CharField(max_length=50, blank=True, null=True)
    endocrine = MultiSelectField(blank=True, null=True, choices=[
        ('Excessive Sweating', 'Excessive Sweating'),
        ('Heat Intolerance', 'Heat Intolerance'),
        ('Polyuria', 'Polyuria'),
        ('Excessive Thirst', 'Excessive Thirst'),
        ('Cold Intolerance', 'Cold Intolerance'),
    ])
    other_endocrine_symptoms = models.CharField(max_length=50, blank=True, null=True)

    '''
    
    Page 3 of the Template

    '''

    # Past Medical History
    past_medical_history = MultiSelectField(blank=True, null=True, choices=[
        ('Primary Koch\'s', 'Primary Koch\'s'),
        ('Asthma', 'Asthma'),
        ('Diabetes', 'Diabetes'),
        ('Hypertension', 'Hypertension'),
        ('Psychiatric Consult', 'Psychiatric Consult'),
        ('Cancer', 'Cancer'),
        ('Prior Surgeries/Hospitalizations', 'Prior Surgeries/Hospitalizations'),
        ('Allergies', 'Allergies'),
    ])
    cancer_site_if_any = models.CharField(max_length=50, blank=True, null=True)
    prior_surgeries_or_hospitalization_dates = models.CharField(max_length=50, blank=True, null=True)
    prior_surgeries_or_hospitalization_reasons = models.CharField(max_length=50, blank=True, null=True)
    allergies = models.CharField(max_length=50, blank=True, null=True)
    other_past_medical_history = models.CharField(max_length=50, blank=True, null=True)

    # Family History
    family_medical_history = MultiSelectField(blank=True, null=True, choices=[
        ('Tuberculosis', 'Tuberculosis'),
        ('Asthma', 'Asthma'),
        ('Psychiatric Consult', 'Psychiatric Consult'),
        ('Diabetes', 'Diabetes'),
        ('Cardiovascular Disease', 'Cardiovascular Disease'),
        ('Cancer', 'Cancer'),
        ('Allergies', 'Allergies'),
    ])
    family_history_cardiovascular_disease = models.CharField(max_length=50, blank=True, null=True)
    family_history_cancer_site = models.CharField(max_length=50, blank=True, null=True)
    family_history_relationship_to_cancer_patient = models.CharField(max_length=50, blank=True, null=True)
    family_history_allergies = models.CharField(max_length=50, blank=True, null=True)
    other_family_history = models.CharField(max_length=50, blank=True, null=True)

    genogram = models.TextField(blank=True, null=True)

    social_and_environmental_history = models.TextField(blank=True, null=True)

    # Gynecologic History
    lmp = models.DateField(blank=True, null=True)
    pmp = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    interval = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    menarche = models.CharField(max_length=50, blank=True, null=True)
    coitarche = models.CharField(max_length=50, blank=True, null=True)

    # Immunization
    complete_immunizations = MultiSelectField(blank=True, null=True, choices=[
        ('DPT/Polio', 'DPT/Polio'),
        ('HIB', 'HIB'),
        ('Hepatitis B', 'Hepatitis B'),
        ('MMR', 'MMR'),
        ('Measles', 'Measles'),
        ('Varicella', 'Varicella'),
        ('Pneumococcal', 'Pneumococcal'),
        ('Influenza', 'Influenza'),
        ('Hepatitis A', 'Hepatitis A'),
    ])
    no_immunization = MultiSelectField(blank=True, null=True, choices=[
        ('DPT/Polio', 'DPT/Polio'),
        ('HIB', 'HIB'),
        ('Hepatitis B', 'Hepatitis B'),
        ('MMR', 'MMR'),
        ('Measles', 'Measles'),
        ('Varicella', 'Varicella'),
        ('Pneumococcal', 'Pneumococcal'),
        ('Influenza', 'Influenza'),
        ('Hepatitis A', 'Hepatitis A'),
    ])
    dpt_or_polio_doses = models.PositiveIntegerField(blank=True, null=True)
    hib_doses = models.PositiveIntegerField(blank=True, null=True)
    hepatitis_b_doses = models.PositiveIntegerField(blank=True, null=True)
    mmr_doses = models.PositiveIntegerField(blank=True, null=True)
    measles_doses = models.PositiveIntegerField(blank=True, null=True)
    varicella_doses = models.PositiveIntegerField(blank=True, null=True)
    pneumococcal_doses = models.PositiveIntegerField(blank=True, null=True)
    influenza_doses = models.PositiveIntegerField(blank=True, null=True)
    hepatitis_a_doses = models.PositiveIntegerField(blank=True, null=True)

    # Adoloscent Interview
    home = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    activities = models.TextField(blank=True, null=True)
    drugs = models.TextField(blank=True, null=True)
    sexual_activity = models.TextField(blank=True, null=True)
    substance_abuse = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    source_of_income_and_dynamics = models.TextField(blank=True, null=True)

    # Medications table has been turned into another model

    additional_details_regarding_history = models.TextField(blank=True, null=True)

    additional_details_regarding_context_including_ethical_considerations = models.TextField(blank=True, null=True)

    '''
    
    Page 4 of the Template

    '''

    # Physical Examination
    height = models.FloatField(help_text="Height in cm", null=True)
    weight = models.FloatField(help_text="Weight in kg", null=True)
    bmi = models.FloatField(blank=True, null=True)
    bp_systolic = models.PositiveIntegerField(blank=True, null=True)
    bp_diastolic = models.PositiveIntegerField(blank=True, null=True)
    hr = models.PositiveIntegerField(blank=True, null=True)
    hr = models.PositiveIntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True, help_text="Temperature in celsius")
    hc = models.FloatField(help_text="in cm", blank=True, null=True)
    cc = models.FloatField(help_text="in cm", blank=True, null=True)
    ac = models.FloatField(help_text="in cm", blank=True, null=True)

    general_state = models.CharField(blank=True, null=True, max_length=9, choices=[
        ('Alert', 'Alert'),
        ('Lethargic', 'Lethargic'),
        ('Obtunded', 'Obtunded'),
        ('Stuporous', 'Stuporous'),
        ('Comatose', 'Comatose'),
    ])

    general_coherence = models.CharField(blank=True, null=True, max_length=10, choices=[
        ('Coherent', 'Coherent'),
        ('Incoherent', 'Incoherent'),
    ])

    pain_scale = models.PositiveIntegerField(blank=True, null=True, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])

    '''
    
    Page 5 of the Template

    '''

    # Neuropsychiatric Exam
    # Mental Status
    general_appearance = models.CharField(blank=True, null=True, max_length=14, choices=[
        ('Well Groomed', 'Well Groomed'),
        ('Fairly Groomed', 'Fairly Groomed'),
        ('Poorly Groomed', 'Poorly Groomed'),
    ])
    general_behavior = models.CharField(blank=True, null=True, max_length=23, choices=[
        ('Normal', 'Normal'),
        ('Psychomotor Retardation', 'Psychomotor Retardation'),
        ('Psychomotor Agitation', 'Poorly Agitation'),
    ])
    attitude_towards_examiner = models.CharField(blank=True, null=True, max_length=13, choices=[
        ('Cooperative', 'Cooperative'),
        ('Uncooperative', 'Uncooperative'),
    ])
    mood = models.CharField(blank=True, null=True, max_length=9, choices=[
        ('Euthymic', 'Euthymic'),
        ('Dysphoric', 'Dysphoric'),
        ('Euphoric', 'Euphoric'),
    ])
    affect = models.CharField(blank=True, null=True, max_length=13, choices=[
        ('Broad', 'Broad'),
        ('Flat', 'Flat'),
        ('Blunted', 'Blunted'),
        ('Restricted', 'Restricted'),
        ('Appropriate', 'Appropriate'),
        ('Inappropriate', 'Inappropriate'),
    ])
    speech = models.CharField(blank=True, null=True, max_length=15, choices=[
        ('Spontaneous', 'Spontaneous'),
        ('Non-spontaneous', 'Non-spontaneous'),
        ('Normoproductive', 'Normoproductive'),
        ('Hypoproductive', 'Hypoproductive'),
        ('Hyperproductive', 'Hyperproductive'),
    ])
    perceptual_disturbance = models.CharField(blank=True, null=True, max_length=17, choices=[
        ('None', 'None'),
        ('Hallucinations', 'Hallucinations'),
        ('Depersonalization', 'Depersonalization'),
        ('Derealization', 'Derealization'),
    ])
    stream_of_thought = models.CharField(blank=True, null=True, max_length=25, choices=[
        ('Goal Oriented', 'Goal Oriented'),
        ('Looseness of Association', 'Looseness of Association'),
        ('Flight of Ideas', 'Flight of Ideas'),
        ('Paucity of Thought', 'Paucity of Thought'),
        ('Tangentiality', 'Tangentiality'),
    ])
    thought_content = models.CharField(blank=True, null=True, max_length=20, choices=[
        ('Normal', 'Normal'),
        ('Paranoia', 'Paranoia'),
        ('Grandiosity', 'Grandiosity'),
        ('Homicidal/Aggression', 'Homicidal/Aggression'),
        ('Bizarre', 'Bizarre'),
        ('Suicidal', 'Suicidal'),
    ])
    impulse_control = models.CharField(blank=True, null=True, max_length=19, choices=[
        ('Able to Control', 'Able to Control'),
        ('Not Able to Control', 'Not Able to Control'),
    ])
    intellectual_capacity_global_estimate = models.CharField(blank=True, null=True, max_length=13, choices=[
        ('Above Average', 'Above Average'),
        ('Average', 'Average'),
        ('Below Average', 'Below Average'),
    ])

    # Sensorium
    consciousness = models.CharField(blank=True, null=True, max_length=6, choices=[
        ('Awake', 'Awake'),
        ('Drowsy', 'Drowsy'),
        ('Stupor', 'Stupor'),
        ('Coma', 'Coma'),
    ])
    other_consciousness = models.CharField(max_length=50, blank=True, null=True)
    attention_span = models.CharField(blank=True, null=True, max_length=9, choices=[
        ('Intact', 'Intact'),
        ('Deficient', 'Deficient'),
    ])
    attention_span_notes = models.CharField(max_length=50, blank=True, null=True)
    orientation_time = models.BooleanField(blank=True, null=True)
    orientation_place = models.BooleanField(blank=True, null=True)
    orientation_person = models.BooleanField(blank=True, null=True)
    memory = models.CharField(blank=True, null=True, max_length=9, choices=[
        ('Intact', 'Intact'),
        ('Deficient', 'Deficient'),
    ])
    memory_notes = models.CharField(max_length=50, blank=True, null=True)
    calculation = models.CharField(blank=True, null=True, max_length=9, choices=[
        ('Intact', 'Intact'),
        ('Deficient', 'Deficient'),
    ])
    calculation_notes = models.CharField(max_length=50, blank=True, null=True)
    fund_of_information = models.CharField(blank=True, null=True, max_length=9, choices=[
        ('Intact', 'Intact'),
        ('Deficient', 'Deficient'),
    ])
    fund_of_information_notes = models.CharField(max_length=50, blank=True, null=True)
    insight = models.CharField(blank=True, null=True, max_length=9, choices=[
        ('Intact', 'Intact'),
        ('Deficient', 'Deficient'),
    ])
    insight_notes = models.CharField(max_length=50, blank=True, null=True)
    judgment = models.CharField(blank=True, null=True, max_length=4, choices=[
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    ])
    planning = models.CharField(blank=True, null=True, max_length=9, choices=[
        ('Intact', 'Intact'),
        ('Deficient', 'Deficient'),
    ])
    planning_notes = models.CharField(max_length=50, blank=True, null=True)

    '''
    
    Page 6 of the Template

    '''

    speech = models.CharField(blank=True, null=True, max_length=10, choices=[
        ('Normal', 'Normal'),
        ('Not Normal', 'Not Normal'),
        ('Dysphonia', 'Dysphonia'),
        ('Dysarthria', 'Dysarthria'),
        ('Dysprosody', 'Dysprosody'),
        ('Dysphasia', 'Dysphasia'),
    ])
    speech_others = models.CharField(max_length=50, blank=True, null=True)
    other_high_cortical_functions = models.CharField(blank=True, null=True, max_length=7, choices=[
        ('Agnosia', 'Agnosia'),
        ('Apraxia', 'Apraxia'),
    ])
    glasgow_coma_scale_gcs = models.PositiveIntegerField(blank=True, null=True, validators=[
        MaxValueValidator(15),
        MinValueValidator(3)
    ])
    glasgow_coma_scale_e = models.PositiveIntegerField(blank=True, null=True, validators=[
        MaxValueValidator(4),
        MinValueValidator(1)
    ])
    glasgow_coma_scale_v = models.PositiveIntegerField(blank=True, null=True, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    glasgow_coma_scale_m = models.PositiveIntegerField(blank=True, null=True, validators=[
        MaxValueValidator(6),
        MinValueValidator(1)
    ])

    # Cranial Nerves
    # Optic Group
    ptosis = models.CharField(blank=True, null=True, max_length=7, choices=[
        ('Absent', 'Absent'),
        ('Present', 'Present'),
    ])
    ptosis_notes = models.CharField(max_length=50, blank=True, null=True)
    gaze = models.CharField(blank=True, null=True, max_length=12, choices=[
        ('Conjugate', 'Conjugate'),
        ('Dysconjugate', 'Dysconjugate'),
    ])
    gaze_notes = models.CharField(max_length=50, blank=True, null=True)
    
    # Brachiomotor Group and Tongue
    masseter_and_temporalis_muscle_bulk_and_strength_v = models.CharField(max_length=50, blank=True, null=True)
    facial_muscles_bulk_and_strength_vii = models.CharField(max_length=50, blank=True, null=True)
    swallowing_ix_x = models.CharField(blank=True, null=True, max_length=10, choices=[
        ('Normal', 'Normal'),
        ('Not Normal', 'Not Normal'),
    ])
    swallowing_notes_ix_x = models.CharField(max_length=50, blank=True, null=True)
    gag_reflex_ix_x = models.CharField(blank=True, null=True, max_length=10, choices=[
        ('Normal', 'Normal'),
        ('Not Normal', 'Not Normal'),
    ])
    gag_reflex_notes_ix_x = models.CharField(max_length=50, blank=True, null=True)
    palatal_elevation_ix_x = models.CharField(blank=True, null=True, max_length=10, choices=[
        ('Normal', 'Normal'),
        ('Not Normal', 'Not Normal'),
    ])
    palatal_elevation_notes_ix_x = models.CharField(max_length=50, blank=True, null=True)
    tongue_protrusion_atrophy_fasciculations_xii = models.CharField(blank=True, null=True, max_length=7, choices=[
        ('Absent', 'Absent'),
        ('Present', 'Present'),
    ])
    tongue_protrusion_atrophy_fasciculations_notes_xii = models.CharField(max_length=50, blank=True, null=True)
    scm_and_trapezius_contour_and_strength_xi = models.CharField(blank=True, null=True, max_length=10, choices=[
        ('Normal', 'Normal'),
        ('Not Normal', 'Not Normal'),
    ])
    scm_and_trapezius_contour_and_strength_notes_xi = models.CharField(max_length=50, blank=True, null=True)

    # Special Sensory Organ Group
    olfaction_i = models.CharField(max_length=100, blank=True, null=True)
    taste_vii = models.CharField(max_length=100, blank=True, null=True)
    schwabach_viii = models.CharField(max_length=100, blank=True, null=True)
    rinnes_viii = models.CharField(max_length=100, blank=True, null=True)
    webers_viii = models.CharField(max_length=100, blank=True, null=True)
    nystagmus = models.CharField(max_length=100, blank=True, null=True)
    
    # Somatic Sensations of the Face
    corneals = models.CharField(max_length=100, blank=True, null=True)
    v1 = models.CharField(max_length=100, blank=True, null=True)
    v2 = models.CharField(max_length=100, blank=True, null=True)
    v3 = models.CharField(max_length=100, blank=True, null=True)

    # Somatic Motor Systems
    gait_and_posture = models.CharField(max_length=100, blank=True, null=True)
    muscle_hypertrophy_or_atrophy = models.CharField(max_length=100, blank=True, null=True)
    involuntary_movements = models.CharField(max_length=100, blank=True, null=True)
    muscle_tone = models.CharField(max_length=100, blank=True, null=True)
    cerebellars = models.CharField(help_text="Indicate FTNT, rebound, rapid alternating hand movements, heel-to-knee",
        max_length=100, blank=True, null=True)
    # Nerve Root Stretching Test
    laseagues = models.CharField(blank=True, null=True, max_length=8, choices=[
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
    ])
    kernigs = models.CharField(blank=True, null=True, max_length=8, choices=[
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
    ])
    meningeals = models.CharField(blank=True, null=True, max_length=8, choices=[
        ('Supple', 'Supple'),
        ('Rigid', 'Rigid'),
    ])
    meningeals_notes = models.CharField(max_length=50, blank=True, null=True)
    
    # Deep Sensory Modalities
    vibratory_sense = models.TextField(blank=True, null=True)
    position_sense = models.TextField(blank=True, null=True)
    rombergs = models.TextField(blank=True, null=True)
    stereognosis = models.TextField(blank=True, null=True)

    '''
    
    Page 7 of the Template

    '''

    patient_education = models.TextField(blank=True, null=True)
    preventive_measures = models.TextField(blank=True, null=True)
    therapeutic_plan = models.TextField(blank=True, null=True)
    diagnostic_plan = models.TextField(blank=True, null=True)
    basis = models.TextField(blank=True, null=True)
    problem_or_impression = models.TextField(blank=True, null=True)
    
    '''
    
    Original Fields

    '''

    language = models.CharField(null=True, max_length=7, choices=[
        ('English', 'English'),
        ('Tagalog', 'Tagalog'),
        ('Taglish', 'Taglish'),
    ])

    provocation = models.CharField(max_length=50, null=True)
    quality = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    severity = models.CharField(max_length=50, null=True)
    timing = models.CharField(max_length=50, null=True)
    background = models.CharField(max_length=200, blank=True, null=True)
    family_history = models.CharField(max_length=200, blank=True, null=True)
    lifestyle = models.CharField(max_length=200, blank=True, null=True)
    recent_interactions = models.CharField(max_length=200, blank=True, null=True)
    medical_history = models.CharField(max_length=200, blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    illness_to_be_diagnosed = models.CharField(max_length=255, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(default='images/gpt.jpg/', max_length=50, blank=True, null=True)

    '''
    
    Tags for the Mentor AI: Relevance & Accuracy

    '''
    relevance = models.TextField(help_text="Fields relevant to the patient's current illness", 
        blank=True, null=True)
    accuracy = models.TextField(help_text="Which fields does the patient have accurate knowledge about?", 
        blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Patient_Medications(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.CharField(max_length=50, null=True)
    generic_name = models.CharField(max_length=50, null=True)
    dosage = models.PositiveIntegerField(blank=True, null=True)
    route = models.CharField(max_length=50, null=True)

class Diagnosed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    conversation = models.TextField(blank=True, null=True)
