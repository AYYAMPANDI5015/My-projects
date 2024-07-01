import streamlit as st
import google.generativeai as genai


GOOGLE_API_KEY="AIzaSyDvwGxjRT7geplMNgd1CfaI7sxKMoDZcoc"
genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')
def main():
   st.set_page_config(page_title="SQL Query Generator")
   st.markdown(
    """
         <div style="text-align:center">
             <h1 style="color:blue">SQL QUERY GENERATOR</h1>
              <h3> I can generate SQL Queries for you!</h3>
               <h4>With Explanation as Well!!!</h4>
               <p>This Tool is a simple tool that allows you to generate SQL queries based on your prompts.</p>
          </div>
      """,
      unsafe_allow_html=True ,
   )
   
   
   text_input=st.text_area("Enter your Query in plain English:")
   
   
   submit=st.button("generate SQl Query")
   if submit:
        with st.spinner("Generating sql Query..."):
            template="""
               Create a SQL query snippet using the below text
         
              ...
         
             {text_input}
             
              ...
         
              I just want a SQL Query.
         
            """
            formatted_template=template.format(text_input=text_input) 
            st.write(formatted_template)
            res=model.generate_content(formatted_template)
            sql=res.text
            st.write(sql)
            
            expected_output="""
                what would be the expected response of this sql query snippet:
                ...
                {sql}
                ...
                provide a sample tabular response with no explanation:
            """
            expected_output_formatted=expected_output.format(sql=sql)
            eop=model.generate_content(expected_output_formatted)
            eop=eop.text
            
            explanation="""
                explain this sql query:
                ...
                {sql}
                ...
              please provide with simplest of explanation:
              """
            explanation_formatted=explanation.format(sql=sql)
            explanation=model.generate_content(explanation_formatted)
            explanation=explanation.text
            
            with st.container():
                st.success("sql query generated successfully")
                st.code(sql,language="sql")
        
main()  