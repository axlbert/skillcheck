import streamlit as st
max_width = 80
padding_top = 1
padding_right = 5
padding_left = 5
padding_bottom = 20
color ='Black'
backgr = 'white'

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {max_width}vw;
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
    .reportview-container .main {{
        color: {color};
        background-color: {backgr};
    }}
</style>
""",
        unsafe_allow_html=True,
    )
categories = ['Fullstack','Project Manager']

questions = { 'Fullstack' : 
                [
                [
                    {'category' : 'Iteration'},
                    {'text' : 'Implements quickly and correctly. Demonstrates regular, incremental, and visible progress. Avoids coupling and over-architecting. Adjusts well to feedback and changing priorities. *Note: Iteration means tangible implementations and designs with which others can interact.'},
                ]
                     ,
                [ 
                    {'category' : 'Specifies, organizes and anticipates'},
                    {'text' : 'Turns difficult problems and underspecified goals into achievable projects. Anticipates dependencies and needs of stakeholders (other teams, users, customers). Defines success and how it will be measured. Creates plans and roadmaps as needed.'},
                ]
                   ,
                    [
                    {'category' : 'Self-motivated learning'},
                    {'text' : 'Learns diverse technologies, techniques and topics out of curiosity. Dives deeper into known stacks. Uses learning to improve our code and processes.'},
                    ] 
                ,
                    [
                    {'category' : 'Public artifacts'},
                    {'text' : 'Creates publicly-viewable artifacts intended for the benefit of others. Examples: participates on Stack sites (including meta), writes blog posts, contributes to open source or apps, speaks at meetups or conferences.'},
                    ]
                ,
                    [
                    {'category' : 'Recruiting, mentoring and teaching'},
                    {'text' : 'Gets involved with recruiting process, such as outreach, screening and interviews. Takes an active interest in new hires and onboarding. Participates in mentoring programs, internally or externally. Works to educate non-technical teams.'},
                    ] 
                ,
                    [
                    {'category' : 'Ideas'},
                    {'text' : 'Consistently coming up with new, useful ideas. Asks questions and fights status quo bias. Thinks independently. Creates new proposals and constructively participates in others’. (Ideas may be expressed via many platforms, such as InVision or Basecamp.)'},
                    ] 
                ,
                    [
                    {'category' : 'Communication'},
                    {'text' : 'Conveys concepts, suggestions, and goals within and across teams. Is proactive about keeping others up to date (peers, managers, stakeholders). Articulates and persuades. Doesn’t “fall off the map”. Uses tools (Trello, chat, calendar, email, docs...) effectively.'},
                    ] 
                 ,
                    [
                    {'category' : 'Database'},
                    {'text' : 'Displays expertise in the databases we use. Very strong at SQL language and performance (including indexes and execution plans). Effective use of Redis. Good understanding of Elastic, as appropriate. Databases used elsewhere can be considered, too.'},
                    ] 
                 ,
                    [
                    {'category' : 'Developer tools'},
                    {'text' : 'Highly proficient at Visual Studio and productivity tools (SSMS, version control, build processes, refactoring & analysis). Strong testing orientation. Consistently looking for ways to increase one’s own productivity and code quality, and those of the team.'},
                    ] 
                 ,
                    [
                    {'category' : 'UX/UI Design'},
                    {'text' : 'Does what it takes to ensure a good user experience. Articulates use cases. Where applicable, works well with designers, understands the vocabulary, and implements designs faithfully.'},
                    ] 
                 ,
                    [
                    {'category' : 'Performance and optimization'},
                    {'text' : 'Does what it takes to ensure a high-performance application (proactively and reactively). Takes an active and consistent interest in profiling and monitoring. Considers performance tuning part of the shipping process.'},
                    ] 
                 ,
                    [
                    {'category' : 'Operational awareness'},
                    {'text' : 'Ensures that [your team here]’s interests are well understood by SREs and vice-versa. Proactively communicates with SRE and works on issues issues such as availability, backups, monitoring, logging, and documentation.'},
                    ] 
                ,
                    [
                    {'category' : 'Security'},
                    {'text' : 'Well-versed in security risks (XSS, SQL injection), knows how they happen and how to avoid them. Responds to security reports quickly. Understands the security guarantees that frameworks do and don’t offer. Avoids unsafe patterns in new code. Aware of and familiar with OWASP Top 10.'},
                    ] 
                ,
                    [
                    {'category' : 'Web programming'},
                    {'text' : 'Expert at full-stack programming, including HTTP, MVC, Ajax, JavaScript, HTML, CSS, IIS / self-hosting. Understands the code and protocols beneath these abstractions and frameworks.'},
                    ] 
                ,
                    [
                    {'category' : 'JavaScript "Stack"'},
                    {'text' : 'Expert at JS and React semantics,all the libraries and frameworks around it.'},
                    ] 
                ],
        'Project Manager' :
        [
            
            [
                {'category' : 'Strategic thinking'},
                {'text' : 'Understands and helps define the overarching, big picture goals for the product (or the part you own) as a whole. Yours, execs’ other’s ideas, it doesn’t matter. Combining all these ideas into a clear, well-defined strategy for your team and product.'},
            ],
            [
                {'category' : 'Ideation and determining what to do now'},
                {'text' : 'Consistently coming up with new, great ideas, or taking others’ ideas to the next level. How do we prioritize good ideas and feature proposals? Balancing cost/benefit, seeing which problems fit into bigger themes, importance vs. urgency, how to keep small improvements happening, etc.'},
            ],
            [
                {'category' : 'Business acumen'},
                {'text' : 'Understands and helps define where product decisions affect the business as a whole. Includes and understands the business requirements in roadmaps and specs. Depending on the situation, this may mean Careers Sales, Marketing, Ad Sales, etc.'},
            ],
            [
                {'category' : 'Spec writing & defining problems/goals'},
                {'text' : 'Takes vague ideas and figures them out. Particular emphasis clear problem statements and what we hope to achieve. Functional Specs, Design Patterns, Problem Statements, RFCs. Clarity and completeness of spec, as well as ability to pitch to address the relevant audience’s concerns.'},
            ],
            [
                {'category' : 'Testing, learning, and user studies'},
                {'text' : 'Can identify and analyze relevant data (internal & external tools, user testing, studies, interviews, etc.), both to determine baselines and what to do AND to test efficacy of efforts. Doesn’t just launch things, but tests them. Knows how to define & measure KPI’s, and do the data forensics necessary to make decisions. Structures usability tests. Captures and communicates failures and successes broadly.'},
            ],
            [
                {'category' : 'UI & Basic Design'},
                {'text' : 'Knows what elements fit what needs, and has a strong sense for user expectations, flow, page attrition/conversion, etc. Can anticipate what will be intuitive, and has an eye for good design.'},
            ],
            [
                {'category' : 'User empathy/segmentation, and behavioral science'},
                {'text' : 'Understands emotional design, and what motivates user decisions (even when the user doesn’t). Shows empathy for the end user, strives to understand their needs, and can recognize and serve user segments with highly divergent needs. (Noobs, Power Users, Silent Majorities, Employers, Candidates etc.)'},
            ],
            [
                {'category' : 'Product ownership'},
                {'text' : 'Takes pride in being the product expert and owner of their domain. Knows the ins-and-outs of your product and all the edge cases to look for. Knows there are few restrictions on their role and takes advantage of that.'},
            ],
            [
                {'category' : 'Project organization, tracking, & updating'},
                {'text' : 'Uses the tools at their disposal (Trello, Basecamp, chat, calendars) to keep projects on point and running smoothly. Keeps all stakeholders on a project on the same page from inception through launch.'},
            ],
            [
                {'category' : 'Ships (for success)'},
                {'text' : 'Moves fast and gets things in customer’s hands as soon as possible to optimize for success. Can determine when and how broadly to solicit input. Gets hands dirty clicking around new features on dev before they go live.Knows when to test prototypes, go to meta, or just ship. When in doubt, ships and learns, but also knows when an MVP requires extra polish to show the user the value.'},
            ],
            [
                {'category' : 'Delegation, empowerment, & service leadership'},
                {'text' : 'Delegates tasks and ownership to the right people. Empowers devs, CMs, salespeople and designers to take on more, and ensures they have the tools and information needed to get their job done. Takes full responsibility for helping other contributors to deliver. Reliable.'},
            ],
            [
                {'category' : 'Recruiting, mentoring and teaching'},
                {'text' : 'Raises the average quality of those around them. Pushes junior PMs, Devs, and other partners to stretch. Finds new talent, interviews and onboards new hires, and teaches others, inside or outside the team.'},
            ],
            [
                {'category' : 'Meta / community and internal communication'},
                {'text' : 'Keeps users and internal stakeholders involved and up to speed, and knows who’s a stakeholder, and how to secure their buy-in when needed. Does the sales team know the feature before you launch? Has the community been consulted about a new feature? Conveys appreciation, shares credit, and responds to feedback in ways that convey respect for the concerns raised, whether they’re used or not.'},
            ],
            [
                {'category' : 'Extracurricular development/public artifacts'},
                {'text' : 'Keeps up with new trends/tools. Educates themself, incorporating new ideas into the product. Shares learnings (internal and out) for the public, company, or individual team benefit.'},
            ],
            [
                {'category' : 'Self-motivated learning'},
                {'text' : 'Learns diverse technologies, techniques and topics out of curiosity. Dives deeper into known stacks. Uses learning to improve our code and processes.'},
            ]
            
        ]
}

category = st.sidebar.selectbox('Select Role',categories)
st.title('Skill Assessment Form')


scoring = []
number_items = len(questions[category])


for entry in questions[category]:
    with st.beta_container():
        col1, col2 = st.beta_columns(2)
        keygen = entry[0]['category']
        col2.subheader(keygen)
        col2.write(entry[1]['text'])
        rating = col1.slider('Rating:',-2,2, key= keygen)
        scoring.append(rating)

total_score = round(float(sum(scoring)/number_items),2)
st.sidebar.subheader('Score: {}'.format(total_score))