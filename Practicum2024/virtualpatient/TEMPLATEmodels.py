from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# MultiSelectField: https://pypi.org/project/django-multiselectfield/


class Patient(models.Model):
    # Page 2 of the template

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

    dwelling_type = models.CharField(blank=True, null=True, max_length=5, choices=[ 
        ('House', 'House'),
        ('Apartment', 'Apartment'),
    ])
    number_of_rooms = models.PositiveIntegerField(blank=True, null=True) 
    appliances = models.CharField(blank=True, null=True, max_length=5, choices=[ 
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
    religion = models.CharField(blank=True, null=True, max_length=14, choices=[
        ('Roman Catholic', 'Roman Catholic'),
        ('Protestant', 'Protestant'),
        ('Muslim', 'Muslim'),
        ('Iglesia ni Cristo', 'Iglesia ni Cristo'),
        ('Aglipay', 'Aglipay'),
        ('Other', 'Other'),
    ])

    annual_family_income = models.CharField(blank=True, null=True, max_length=8, choices=[
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
    to_a_x_year_old = models.PositiveIntegerField(blank=True, null=True)
    g_mother = models.CharField(max_length=50, blank=True, null=True)
    p_mother = models.CharField(max_length=50, blank=True, null=True)
    bw = models.CharField(max_length=50, blank=True, null=True)
    attended_by_first_name = models.CharField(max_length=50, blank=True, null=True) 
    attended_by_last_name = models.CharField(max_length=50, blank=True, null=True)
    perinatal_cx = models.CharField(max_length=50, blank=True, null=True) 

    # Developmental Milestones
    gross_motor = models.TextField(blank=True, null=True)
    adaptive_fine_motor = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    personal_and_social = models.TextField(blank=True, null=True)

    # Review of Systems
    general = models.MultiSelectField(blank=True, null=True, max_length=7, choices=[
        ('Fever', 'Fever'),
        ('Weight Gain', 'Weight Gain'),
        ('Weight Loss', 'Weight Loss'),
        ('Weakness', 'Weakness'),
        ('Fatigue', 'Fatigue'),
    ])
    other_general_symptoms = models.CharField(max_length=50, blank=True, null=True)
    musculoskeletal_or_dermatologic = models.MultiSelectField(blank=True, null=True, choices=[
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
    heent = models.MultiSelectField(blank=True, null=True, choices=[
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
    respiratory = models.MultiSelectField(blank=True, null=True, max_length=7, choices=[
        ('Dyspnea', 'Dyspnea'),
        ('Hemoptysis', 'Hemoptysis'),
        ('Cough', 'Cough'),
        ('Wheezing', 'Wheezing'),
    ])
    cardiovascular = models.MultiSelectField(blank=True, null=True, max_length=7, choices=[
        ('Palpitations', 'Palpitations'),
        ('Chest Pains', 'Chest Pains'),
        ('Syncope', 'Syncope'),
        ('Orthopnea', 'Orthopnea'),
    ])
    other_cardiovascular_symptoms = models.CharField(max_length=50, blank=True, null=True)
    gastrointestinal = models.MultiSelectField(blank=True, null=True, max_length=7, choices=[
        ('Nausea', 'Nausea'),
        ('Vomiting', 'Vomiting'),
        ('Dysphagia', 'Dysphagia'),
        ('Heartburn', 'Heartburn'),
        ('Change in Bowel Habits', 'Change in Bowel Habits'),
        ('Rectal Bleeding', 'Rectal Bleeding'),
        ('Jaundice', 'Jaundice'),
    ])
    genitourinary = models.MultiSelectField(blank=True, null=True, max_length=7, choices=[
        ('Nocturia', 'Nocturia'),
        ('Dysuria', 'Dysuria'),
        ('Frequency', 'Frequency'),
        ('Hematuria', 'Hematuria'),
    ])
    other_genitourinary_symptoms = models.CharField(max_length=50, blank=True, null=True)

    height = models.FloatField(help_text="Height in cm", null=True)
    weight = models.FloatField(help_text="Weight in kg", null=True)
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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Diagnosed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    conversation = models.TextField(blank=True, null=True)
