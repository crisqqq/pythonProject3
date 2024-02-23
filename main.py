
import os
import pandas as pd
from langchain_community.llms import Tongyi
from langchain_experimental.agents.agent_toolkits import create_csv_agent
os.environ["DASHSCOPE_API_KEY"] = "sk-c66a6df6b0014d0daa9a6cd3975bad20"

# Import necessary libraries
import streamlit as st
import pandas as pd
from langchain.llms import Tongyi
from langchain_experimental.agents.agent_toolkits import create_csv_agent

# Create a function to handle file upload and model execution
def run_model(file, question):
    # Save the uploaded file as a CSV
    df = pd.read_excel(file)
    df.to_csv("file_path2.csv", index=False)

    # Use Tongyi model and agent to run
    agent = create_csv_agent(Tongyi(), 'file_path2.csv', verbose=True)
    result = agent.run(question)
    return result
# Create a web application using Streamlit

def main():
    st.title("智能文件分析")

    # Upload and process file
    file = st.file_uploader("请上传.xlsx表格文件", type=["xlsx"])
    if file is not None:
        question = st.text_input("请输入您要查询的内容")
        result = run_model(file, question)
        st.write("回答:", result)



if __name__ == "__main__":
    main()
