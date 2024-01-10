from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import re

app=Flask(__name__)

headings =("SchemeID", "SchemeName", "EligibilityCriteria", "Details", "Benefits", "StartDate", "EndDate", "Department")
dataW = (
     (1, 'Women''s Education Empowerment', 'Women pursuing higher education', 'Provides scholarships and financial assistance', 'Tuition fee coverage, mentorship programs', '2024-06-01', '2025-05-31', 'Ministry of Education'),

    (2, 'Maternal Healthcare Support', 'Pregnant women and new mothers', 'Ensures access to quality maternal healthcare services', 'Prenatal care, postnatal care, vaccinations', '2024-07-01', '2024-12-31', 'Ministry of Health'),

    (3, 'Women''s Entrepreneurship Development', 'Aspiring women entrepreneurs', 'Facilitates skill development and business support', 'Training programs, startup grants, mentorship', '2024-08-01', '2025-07-31', 'Ministry of Small and Medium Enterprises'),

    (4, 'Gender Equality in the Workplace', 'Working women facing discrimination', 'Promotes gender equality and addresses workplace bias', 'Equal pay initiatives, anti-discrimination training', '2024-09-01', '2025-08-31', 'Ministry of Labor'),

    (5, 'Rural Women Development Fund', 'Rural women involved in agriculture or cottage industries', 'Supports rural women in economic activities', 'Agricultural training, financial aid, infrastructure development', '2024-10-01', '2025-05-31', 'Ministry of Rural Development'),

    (6, 'Women''s Health Awareness Program', 'All women in the community', 'Promotes health awareness and preventive care', 'Health screenings, workshops, informational campaigns', '2024-11-01', '2024-11-30', 'Ministry of Health'),

    (7, 'Skill Development for Single Mothers', 'Single mothers and caregivers', 'Provides training for employable skills', 'Vocational training, job placement assistance', '2025-01-01', '2025-01-31', 'Ministry of Women and Child Development'),

    (8, 'Women in Science Scholarship', 'Female students pursuing STEM fields', 'Encourages women to pursue careers in science', 'Scholarship funds, mentorship by women scientists', '2025-02-01', '2025-02-28', 'Ministry of Science and Technology'),

    (9, 'Domestic Violence Support Helpline', 'Women facing domestic violence', 'Provides a helpline for counseling and support', 'Crisis intervention, legal aid referrals', '2025-03-01', '2025-03-31', 'Ministry of Social Justice'),

    (10, 'Women''s Empowerment in Agriculture', 'Women involved in agriculture', 'Promotes sustainable farming practices and market access', 'Training, agricultural resources, market linkages', '2025-04-01', '2025-04-30', 'Ministry of Agriculture'),

    (11, 'Financial Literacy for Women', 'Women in low-income communities', 'Educates women on financial management and entrepreneurship', 'Financial literacy workshops, access to microfinance', '2025-05-01', '2025-05-31', 'Ministry of Finance'),

    (12, 'Sports Scholarship for Women', 'Female athletes pursuing sports at the national level', 'Supports talented women in sports', 'Scholarship funds, specialized training', '2025-06-01', '2025-06-30', 'Ministry of Youth Affairs and Sports'),

    (13, 'Urban Women Housing Subsidy', 'Urban women from economically weaker sections', 'Provides financial assistance for housing', 'Subsidized housing loans, affordable housing projects', '2025-07-01', '2025-07-31', 'Ministry of Urban Development'),

    (14, 'Artisan Empowerment Program', 'Women engaged in traditional crafts and artisanal work', 'Preserves and promotes traditional crafts', 'Skill development, market access, cultural events', '2025-08-01', '2025-08-31', 'Ministry of Culture'),

    (15, 'Women''s Mental Health Initiative', 'Women dealing with mental health challenges', 'Addresses mental health issues and provides support', 'Counseling services, awareness campaigns', '2025-09-01', '2025-09-30', 'Ministry of Health')
)

@app.route("/")
def table():

    return render_template("women.html", headings=headings, data=dataW)


headings =("SchemeID", "SchemeName", "EligibilityCriteria", "Details", "Benefits", "StartDate", "EndDate", "Department")
dataT = (
     (1, 'Transgender Education Scholarship', 'Transgender individuals pursuing higher education', 'Provides financial assistance for tuition and living expenses', 'Scholarship funds, mentorship programs', '2024-06-01', '2025-05-31', 'Ministry of Education'),

    (2, 'Healthcare Equality Program', 'All transgender individuals', 'Ensures access to gender-affirming healthcare services', 'Medical consultations, hormone therapy, gender-affirming surgeries', '2024-07-01', '2024-12-31', 'Ministry of Health'),

    (3, 'Transgender Employment Support', 'Unemployed transgender individuals', 'Assists in finding employment opportunities and skill development', 'Job placement services, vocational training programs', '2024-08-01', '2025-07-31', 'Ministry of Labor'),

    (4, 'Housing Rights for Transgender Individuals', 'Transgender individuals facing housing discrimination or homelessness', 'Provides housing assistance and legal support', 'Temporary shelters, rental assistance, legal aid', '2024-09-01', '2025-08-31', 'Ministry of Social Justice'),

    (5, 'Transgender Cultural Empowerment Grant', 'Transgender individuals involved in promoting cultural awareness', 'Supports cultural projects and events that celebrate transgender diversity', 'Grant funding for events, workshops, and artistic projects', '2024-10-01', '2025-05-31', 'Ministry of Culture'),

    (6, 'Transgender Mental Health Support', 'Transgender individuals dealing with mental health challenges', 'Addresses mental health issues and provides counseling services', 'Therapy sessions, support groups, awareness campaigns', '2024-11-01', '2024-11-30', 'Ministry of Health'),

    (7, 'Transgender Entrepreneurship Development', 'Transgender individuals interested in starting businesses', 'Facilitates skill development and business support', 'Training programs, startup grants, mentorship', '2025-01-01', '2025-01-31', 'Ministry of Small and Medium Enterprises'),

    (8, 'Legal Aid for Transgender Rights', 'Transgender individuals facing legal challenges', 'Provides legal assistance for issues related to transgender rights', 'Legal consultations, representation in court', '2025-02-01', '2025-02-28', 'Ministry of Law'),

    (9, 'Transgender Sports Inclusion Program', 'Transgender athletes aspiring to compete', 'Promotes inclusion in sports for transgender individuals', 'Training facilities, participation in sporting events', '2025-03-01', '2025-03-31', 'Ministry of Youth Affairs and Sports'),

    (10, 'Transgender Skill Development in Arts', 'Transgender individuals interested in arts and culture', 'Supports skill development in various artistic disciplines', 'Workshops, exhibitions, cultural events', '2025-04-01', '2025-04-30', 'Ministry of Culture'),

    (11, 'Transgender Community Health Clinics', 'All transgender individuals', 'Establishes community health clinics for transgender-specific healthcare', 'Primary care, counseling services, outreach programs', '2025-05-01', '2025-05-31', 'Ministry of Health')

    (12, 'Transgender Employment Equality Initiative', 'Transgender individuals in the workforce', 'Promotes equal employment opportunities and workplace inclusion', 'Employment workshops, diversity training for companies', '2025-06-01', '2025-06-30', 'Ministry of Labor'),

    (13, 'Transgender Housing Assistance Program', 'Transgender individuals facing housing challenges', 'Provides financial aid for housing and rental assistance', 'Temporary housing support, legal aid for housing issues', '2025-07-01', '2025-07-31', 'Ministry of Social Justice'),

    (14, 'Transgender Youth Education Outreach', 'Transgender youth in schools and colleges', 'Creates awareness and support systems for transgender students', 'Educational workshops, counseling services', '2025-08-01', '2025-08-31', 'Ministry of Education'),

    (15, 'Transgender Arts and Culture Festival', 'All transgender individuals with an interest in arts and culture', 'Celebrates transgender creativity and diversity through a cultural festival', 'Art exhibitions, performances, workshops', '2025-09-01', '2025-09-30', 'Ministry of Culture')
)

@app.route("/")
def table():

    return render_template("trans.html", headings=headings, data=dataT)






if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)