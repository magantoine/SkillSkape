PROMPTS = {
    "INIT": {
        "system": "You are an expert human resource manager. You need to analyse skills in a job posting.",
        "instruction": "You are an expert human resource manager. You are given an extract from a job description and a skill coming from ESCO. Highlight all the parts of the job description that relates to the given skill, by surrounding them with tags '@@' at the beginning and '##' at the end. You should rewrite the entire sentence. The highlighted parts should precisely talk about the given skills and only this skills. The higlighted parts must precisely be about the given skills. Do not highlight parts not related to it. The sentence should be rewritten perfectly, using the same exact same words. You must highlight at least one part in the sentence that you will rewrite. The highlighted part should be as short as possible.\n",
        "shots": [
            "Sentence: We are seeking a highly skilled individual who is experienced in conducting comprehensive scientific inquiries and proficient in interpreting and synthesizing complex test results for our research and development department.\nskill: analyse test data.\nAnswer: We are seeking a highly skilled individual who is experienced in @@conducting comprehensive scientific inquiries## and proficient in interpreting and synthesizing complex test results for our research and development department.\n",
            "Sentence: We are seeking a meticulous Data Analyst to join our team. As a Data Analyst, you will be responsible for ensuring the accuracy and integrity of our data by normalizing and standardizing it. You will utilize your expertise in data normalization techniques to identify and resolve inconsistencies, ensuring that our data is reliable and consistent across all systems. In addition, you will collaborate with cross-functional teams to design and implement data normalization processes that optimize data quality and improve overall efficiency. The ideal candidate will have a strong understanding of data normalization methodologies and the ability to apply them in a fast-paced and dynamic environment. Attention to detail and a focus on data accuracy are key attributes for success in this role. Join us and make a significant impact on our data integrity initiatives.\nskill: normalise data.\nAnswer: We are seeking a meticulous Data Analyst to join our team. As a Data Analyst, you will be responsible for ensuring the accuracy and integrity of our data by @@normalizing and standardizing it##. You will utilize your expertise in @@data normalization techniques## to identify and resolve inconsistencies, ensuring that our data is reliable and consistent across all systems. In addition, you will collaborate with cross-functional teams to @@design and implement data normalization processes## that optimize data quality and improve overall efficiency. The ideal candidate will have a strong understanding of @@data normalization methodologies## and the ability to apply them in a fast-paced and dynamic environment. Attention to detail and a focus on data accuracy are key attributes for success in this role. Join us and make a significant impact on our data integrity initiatives.\n",
            "Sentence: the ability to work collaboratively across disciplines is a key criterion for this position.\nskill: collaborate with engineers\nAnswer: @@ability to collaborate across disciplines## is a key criterion for this position.\n",
            "Sentence: We are seeking a highly organized and detail-oriented individual to join our team as an Archive Administrator. In this role, you will be responsible for managing our archive system and ensuring that all users adhere to the established guidelines. Your excellent organizational skills will be essential in maintaining accurate and up-to-date records. Additionally, you will collaborate with the IT department to troubleshoot any technical issues related to the archive system. Knowledge of database management and proficiency in data analysis will be an advantage in this position. The ability to prioritize tasks and meet deadlines with precision is a must. If you have a keen eye for detail and a drive for maintaining organized information systems, we welcome your application.\nskill: manage archive users guidelines.\nAnswer: We are seeking a highly organized and detail-oriented individual to join our team as an Archive Administrator. In this role, you will be responsible for @@managing our archive system and ensuring that all users adhere to the established guidelines##. Your excellent organizational skills will be essential in maintaining accurate and up-to-date records. Additionally, you will collaborate with the IT department to troubleshoot any technical issues related to the archive system. Knowledge of database management and proficiency in data analysis will be an advantage in this position. The ability to prioritize tasks and meet deadlines with precision is a must. If you have a keen eye for detail and a drive for maintaining organized information systems, we welcome your application.\n",
        ],  
    },
    "BAD-BOUNDS": {
        "content": "In your response, you highlighted some parts using @@ at the beginning and @@ at the end. Please use @@ at the beginning of the parts and ## at the end of the part you want to highlight. Annotate the previous sentence, but with the correct highlighting."
    },
    "NO-ANNOT": {
        "content": "In your response, you highlighted nothing. Please annotate the previous sentence, and highlight at least one part linked to the skill."
    },
    "FULL-ANNOT": {
        "content": "In your response, you highlighted the entire sentence. Please rewrite the initial sentence and hgihlight a smaller part linked to the skill."
    }

}

REFINE_PROMPT = {
    "system": "You are an expert human resource manager. You need to analyse skills in a job posting.",
    "instruction": "You are an expert human resource manager. You were given a set of skills and you were ask to provide a one-sentence-long job description that contains all the given skills. You were given : {input_skills}. and you gave {gen_sentence}. You should take the previously generated sentence and improve it. To do so you need to add these skills that are not mentioned in your sentence : {forgot_skills}. The final sentence must not contain any of these formulation : {forbid_spans}.\n",
}