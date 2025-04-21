import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('model.pkl')

st.title("Network Intrusion Detection 🚨")

st.subheader("Enter the features below:")

# Create input fields for all features
duration = st.number_input('Duration')
protocol_type = st.number_input('Protocol Type (encoded)')
service = st.number_input('Service (encoded)')
flag = st.number_input('Flag (encoded)')
src_bytes = st.number_input('Source Bytes')
dst_bytes = st.number_input('Destination Bytes')
land = st.number_input('Land')
wrong_fragment = st.number_input('Wrong Fragment')
urgent = st.number_input('Urgent')
hot = st.number_input('Hot')
num_failed_logins = st.number_input('Number of Failed Logins')
logged_in = st.number_input('Logged In (0/1)')
num_compromised = st.number_input('Number Compromised')
root_shell = st.number_input('Root Shell (0/1)')
su_attempted = st.number_input('SU Attempted')
num_root = st.number_input('Number of Roots')
num_file_creations = st.number_input('Number of File Creations')
num_shells = st.number_input('Number of Shells')
num_access_files = st.number_input('Number of Access Files')
is_guest_login = st.number_input('Is Guest Login (0/1)')
count = st.number_input('Count')
srv_count = st.number_input('SRV Count')
serror_rate = st.number_input('Serror Rate')
srv_serror_rate = st.number_input('SRV Serror Rate')
rerror_rate = st.number_input('Rerror Rate')
srv_rerror_rate = st.number_input('SRV Rerror Rate')
diff_srv_rate = st.number_input('Diff SRV Rate')
srv_diff_host_rate = st.number_input('SRV Diff Host Rate')
dst_host_count = st.number_input('Dst Host Count')
dst_host_srv_count = st.number_input('Dst Host SRV Count')
dst_host_diff_srv_rate = st.number_input('Dst Host Diff SRV Rate')
dst_host_same_src_port_rate = st.number_input('Dst Host Same Src Port Rate')
dst_host_serror_rate = st.number_input('Dst Host Serror Rate')
dst_host_srv_serror_rate = st.number_input('Dst Host SRV Serror Rate')
dst_host_rerror_rate = st.number_input('Dst Host Rerror Rate')
dst_host_srv_rerror_rate = st.number_input('Dst Host SRV Rerror Rate')

# Prediction button
if st.button('Predict'):
    input_features = np.array([[duration, protocol_type, service, flag, src_bytes, dst_bytes, land,
                                wrong_fragment, urgent, hot, num_failed_logins, logged_in, num_compromised,
                                root_shell, su_attempted, num_root, num_file_creations, num_shells,
                                num_access_files, is_guest_login, count, srv_count, serror_rate,
                                srv_serror_rate, rerror_rate, srv_rerror_rate, diff_srv_rate,
                                srv_diff_host_rate, dst_host_count, dst_host_srv_count,
                                dst_host_diff_srv_rate, dst_host_same_src_port_rate,
                                dst_host_serror_rate, dst_host_srv_serror_rate,
                                dst_host_rerror_rate, dst_host_srv_rerror_rate]])

    prediction = model.predict(input_features)

    st.success(f'Prediction: {prediction[0]}')
