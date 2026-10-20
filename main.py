import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generate Dummy Data Skenario Usability
np.random.seed(42)
n = 500
age_groups = np.random.choice(['Gen Z', 'Profesional', 'Lansia'], n)
ui_versions = np.random.choice(['Lama (GUI)', 'Baru (Inklusif)'], n)

task_times = []
error_counts = []
successes = []

for i in range(n):
    base_time = 30
    base_error = 1
    
    if age_groups[i] == 'Lansia':
        base_time += 20
        base_error += 2
    elif age_groups[i] == 'Gen Z':
        base_time -= 10
        
    if ui_versions[i] == 'Lama (GUI)':
        base_time += 15
        base_error += 1
    else:
        base_time -= 5
        base_error -= 1
        
    time_spent = max(10, np.random.normal(base_time, 10))
    
    # Anomali/Outlier (misal: user tertinggal/AFK)
    if np.random.rand() < 0.05: 
        time_spent += 100 
        
    errors = max(0, int(np.random.normal(base_error, 1)))
    
    prob_success = 1.0 - (errors * 0.15) - (time_spent * 0.002)
    prob_success = max(0.1, min(0.95, prob_success))
    success = np.random.binomial(1, prob_success)
    
    task_times.append(time_spent)
    error_counts.append(errors)
    successes.append(success)

df = pd.DataFrame({
    'User_ID': range(1, n+1),
    'Persona': age_groups,
    'Versi_UI': ui_versions,
    'Waktu_Tugas_Detik': task_times,
    'Jumlah_Error': error_counts,
    'Sukses': successes
})

# 2. Preprocessing & Pembersihan Anomali
df_clean = df[df['Waktu_Tugas_Detik'] < 100].copy()

# SIMPAN FILE KE CSV (File akan otomatis dibuat di folder ini)
df_clean.to_csv('usability_testing_data.csv', index=False)

# Encode Categorical
df_encoded = pd.get_dummies(df_clean, columns=['Persona', 'Versi_UI'], drop_first=True)

# 3. Modeling Machine Learning
X = df_encoded.drop(['User_ID', 'Sukses'], axis=1)
y = df_encoded['Sukses']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"Akurasi Model Berhasil Dihitung: {acc:.4f}")

# 4. Visualisasi & Simpan Gambar
feat_importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=feat_importances.values, y=feat_importances.index, palette='viridis')
plt.title('Feature Importance: Faktor Keberhasilan Penggunaan Aplikasi', fontweight='bold')
plt.xlabel('Tingkat Kepentingan (Importance)')
plt.ylabel('Fitur')
plt.tight_layout()

# SIMPAN GAMBAR KE PNG (File gambar akan otomatis dibuat di folder ini)
plt.savefig('feature_importance.png')
plt.close()

print("SUKSES! File CSV dan Gambar PNG telah berhasil dibuat di folder proyek.")