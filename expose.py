import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

openai_key = os.getenv('OPENAI_KEY')

from openai import OpenAI
openai_client = OpenAI(api_key=openai_key)

def write_expose(theme) :

    
    
    def chatgpt(instruction, prompt):
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        print(response.choices[0].message.content)
        print('\n-----------------------\n')
        return response.choices[0].message.content


    class ClaudeModel:
        haiku = "claude-3-haiku-20240307"
        sonnet = "claude-3-sonnet-20240229"
        opus = "claude-3-opus-20240229"




    clearn_input_instruction = "Ton role est de nettoyer ce qu’ont envoie et de faire ressortir le thème de l’exposé uniquement de façon clair et avec la formulation correcte. Exemple : 1 - ‘Fait un exposé sur la guerre en Ukraine’ -> ‘Guerre en Ukraine’  2 - exposé sur la guerre en Ukraine -> ‘Guerre en Ukraine’ 3 - ‘Rédige un exposé sur la guerre en Ukraine’ -> ‘Guerre en Ukraine’  4 - La guerre en Ukraine -> ‘Guerre en Ukraine’ 5 - ‘Le vih sda’ -> ‘Le VIH SIDA’ 6 - ‘La pltique en UE’ -> ‘La politique en UE’ 7 - 'Ecris un exposé sur la polique en cote d'ivoire, genre qui parle des politiciens' -> 'La politique et les politiciens en Côte d'Ivoire' - 'activité cérébrale : le cas motricité volontaire' -> 'Les activités cérébrales : le cas de la motricité volontaire' -  'Les activités cérébrales : les aires cérébrales' -> 'Les activités cérébrales : les aires cérébrales'"
    create_main_point_instruction = "Ton rôle est d’aidé une IA qui rédiger des exposés, en reformulant correctement les prompts qui te seront donné. Exemple :  1’ - Ecris un exposé sur les marché noir, qui parle de l'afrique et les divers trafique au seins de ce sontinant’ -> ’Un exposé sur les marchés noirs en Afrique, abordant les diverses formes de trafics illégaux présents sur ce continent’ 2 - ‘Ecris un exposé sur la polique en cote d'ivoire, genre qui parle des politiciens’ ->  ’Un exposé sur la politique en Côte d'Ivoire, en vous concentrant sur les personnalités et les figures politiques marquantes du pays.’-Tu doit tenir compte de ce qu'il te serra dit dans le prompt, integre tout ce qu'il te serra dit dedans. Reformule juste sans commentaire, juste entre guillemet sans rien d'autres"
    create_plan_instruction = "Ton rôle est de générer des plans détaillés pour des exposés. - Chaque plan doit être très détaillé, 3 grandes parties minimum ( Plus si nécéssaire ) - avec un minimum de 3 sous-parties pour chaque grande partie ( Plus si nécéssaire ) . - Donne juste le plan sans aucun commentaire, sans rien dire d'autre. IMPORTANT : Sépare chaque titre avec '%M'. C'est très important. Voici exemple de séparation : Exemple 1: %M* I. Exemple de grand titre 1. Exemple de petit titre Petite resumé... 2. Exemple de petit titre Petite resumé... %M* II. Exemple de grand titre 1. Exemple de petit titre Petite resumé... ... %M*"
    redaction_instruction = "Ton role est de rédiger un exposé a parti du plan qui t’est donner. - IMPORTANT: \n\n1. Mets '<br>' au début et à la fin de chaque titre pour séparation. Exemple : I. Grand titre <br> </strong>  <strong> <br> 1. Petit titre <br> </strong>   \n2. Mets en gras les titres et sous-titres avec '<strong>'. \nExemple : <strong> I. Grand titre <br> </strong>  <strong> <br> 1. Petit titre <br> </strong> \n\n3. Mets '<br>' en début et fin de chaque paragraphe. \nExemple : <br> Redaction... <br> \n\n4. Je te fournirai le plan progressivement. Le thème est : {}.\n\n5. Chaque sous-partie doit contenir 100 mots. \nExemple : \n'<strong> I. GRAND TITRE <br> </strong>\n <strong> <br> 1. sous partie <br> </strong> \n <br> Redaction ( 100 mots ) ... <br>\n <strong> <br> 2. sous partie <br> </strong> \n <br> Redaction ( 100 mots ) ...<br>.'\"\n"



    prompt_user = theme
    print('\n')

    list_plan_exposé = []
    expose_content_split = []

    if prompt_user :
        print('------------------\n')
        theme_expose = chatgpt(clearn_input_instruction, prompt_user)
        create_main_point = chatgpt(create_main_point_instruction, theme_expose)
        create_plan_list = chatgpt(create_plan_instruction, create_main_point).strip().split('%M*')
        for split_plan in create_plan_list:
            list_plan_exposé.append(split_plan)
            expose = chatgpt(redaction_instruction.format(theme_expose), split_plan)
            expose_content_split.append(expose)

    return expose_content_split


