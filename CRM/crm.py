import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout="wide")
st.title("📊 CRM 리드 예측 기반 대시보드 (Target: Status_Text)")

uploaded_file = st.file_uploader("CSV 파일 업로드 (Status_Text 포함)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("데이터가 성공적으로 업로드되었습니다!")

    # 열 미리 보기
    st.subheader("📌 데이터 열 미리 보기")
    st.write(df.columns.tolist())

    if 'Status_Text' not in df.columns:
        st.error("❗ 'Status_Text' 열이 필요합니다. CSV 파일을 확인해주세요.")
    else:
        st.markdown("---")

        # 타겟 분포
        st.subheader("📈 타겟 상태(Status_Text) 분포")
        fig1, ax1 = plt.subplots()
        sns.countplot(data=df, x='Status_Text', order=df['Status_Text'].value_counts().index, ax=ax1)
        ax1.set_title("Status_Text 분포")
        plt.xticks(rotation=45)
        st.pyplot(fig1)

        # 원형 차트
        st.subheader("🌍 원형 분포 시각화")
        fig1_pie, ax_pie = plt.subplots()
        df['Status_Text'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax_pie)
        ax_pie.set_ylabel('')
        st.pyplot(fig1_pie)

        # 상태별 수치형 변수 평균 비교
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if numeric_cols:
            st.subheader("📊 상태별 주요 수치 지표 평균 비교")
            selected_num = st.selectbox("비교할 수치형 열 선택", numeric_cols)
            fig2, ax2 = plt.subplots()
            sns.barplot(data=df, x='Status_Text', y=selected_num, estimator='mean', ax=ax2)
            ax2.set_title(f"Status_Text 별 평균 {selected_num}")
            plt.xticks(rotation=45)
            st.pyplot(fig2)

            # Boxplot
            st.subheader("🔹 상태별 Boxplot 보기")
            fig2b, ax2b = plt.subplots()
            sns.boxplot(data=df, x='Status_Text', y=selected_num, ax=ax2b)
            ax2b.set_title(f"{selected_num} 보기 범위")
            plt.xticks(rotation=45)
            st.pyplot(fig2b)

        # 상태별 카테고리 변수 비교
        categorical_cols = df.select_dtypes(include='object').columns.tolist()
        categorical_cols = [col for col in categorical_cols if col != 'Status_Text']
        if categorical_cols:
            st.subheader("📊 상태별 카테고리 변수 분포 비교")
            selected_cat = st.selectbox("비교할 범주형 열 선택", categorical_cols)
            fig3, ax3 = plt.subplots()
            sns.countplot(data=df, x=selected_cat, hue='Status_Text', order=df[selected_cat].value_counts().index[:10], ax=ax3)
            ax3.set_title(f"{selected_cat} 별 Status_Text 분포")
            plt.xticks(rotation=45)
            st.pyplot(fig3)

        # Pairplot
        if len(numeric_cols) >= 2:
            st.subheader("🔸 수치형 열 간 상관관계 (Pairplot)")
            selected_pair = st.multiselect("2~4개 수치형 열 선택", numeric_cols, default=numeric_cols[:2])
            if 2 <= len(selected_pair) <= 4:
                fig4 = sns.pairplot(df, vars=selected_pair, hue='Status_Text')
                st.pyplot(fig4)

        # 데이터 테이블
        st.subheader("🧾 데이터 미리보기")
        st.dataframe(df.head(100))

else:
    st.info("CSV 파일을 업로드하면 분석이 시작됩니다.")