#FORMS


#import streamlit as st
#import spacy
#
#nlp =  spacy.load("en_core_web_lg")
#
#def extract_ents(ent_types,text,nlp):
#
#    doc = nlp(text)
#    results = list()
#    for ent in doc.ents:
#        print(ent.label_,ent.text)
#        if ent.label_ in ent_types:
#            results.append((ent.text,ent.label_))
#
#
#    print(results)
#    return results
#
#
#st.title(" FORMS DEMONSTRATION ")
#
#st.sidebar.header("params")
#ent_types =  st.sidebar.multiselect("select entities",["PERSON","LANGUAGE","GPE"])
#
#text = st.text_area("write the text here" ,"Mr. Marek plays something in new york and he speaks english.")
#
#if st.button("get entities"):
#
#    hits = extract_ents(ent_types, text, nlp)
#    st.write(hits)


#Problem streamlit reruns the whole program  whenever there is an interaction of the user with the app therefore we will use forms


import streamlit as st
import spacy
import time
import en_core_web_lg

@st.cache(allow_output_mutation=True) #hashing problems consult documentation
def load_model(model):
    print(f" loading Model- {model}-......")
    return spacy.load(model)


#print("loading model outside cache")
#start_time = time.time()
#nlp = spacy.load("en_core_web_lg")
#print("loading model outside cache -- [DONE] %s seconds ---" % (time.time() - start_time))

nlp = load_model("en_core_web_lg")



def extract_ents(ent_types,text,nlp):

    doc = nlp(text)
    results = list()
    for ent in doc.ents:
        print(ent.label_,ent.text)
        if ent.label_ in ent_types:
            results.append((ent.text,ent.label_))


    print(results)
    return results


st.title(" FORMS DEMONSTRATION ")

form_1  = st.sidebar.form(key="something_unique")
form_1.header("params")
ent_types =  form_1.multiselect("select entities",["PERSON","LANGUAGE","GPE"])

text = st.text_area("write the text here" ,"Mr. Marek works at Google  in new york and he speaks english.")

if form_1.form_submit_button("get entities"):

    hits = extract_ents(ent_types, text, nlp)
    st.write(hits)
