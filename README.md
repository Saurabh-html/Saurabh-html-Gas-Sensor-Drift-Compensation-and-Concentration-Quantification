# Gas Sensor Drift Compensation using Machine Learning


## 📌 Overview
This project addresses **sensor drift** in metal oxide semiconductor (MOS) gas sensors using a **Random Forest Regressor**. Designed for industrial IoT applications, the framework compensates for long-term drift across six gases (Ammonia, Acetaldehyde, Acetone, Ethylene, Ethanol, Toluene) over 36 months. The model achieves **<10% MAE** and reduces recalibration frequency by **40%** compared to traditional systems.

## 🚀 Key Features
- **Drift-Resistant Architecture**: Prioritizes transient sensor dynamics (EMA features) over steady-state responses.
- **Multi-Gas Validation**: Tested on 13,910 measurements from 16 sensors.
- **Edge Compatibility**: 5 ms inference time on resource-constrained devices.
- **Batch-Wise Analysis**: Performance tracking across 10 temporal batches.

## 📊 Results
| Metric          | Validation Set | Test Set      |
|-----------------|----------------|---------------|
| **R² Score**    | 0.997          | 0.969         |
| **MSE**         | 78.12          | 901.07        |

![Feature Importance](media/feature_importance.png) <!-- Add feature importance plot -->
*Top drift-resistant features: Sensor 106 (32.4%) and Sensor 98 (21.5%).*

![Batch Performance](media/batch_performance.png) <!-- Add batch-wise R² plot -->
*R² degradation from 0.98 (Batch 1) to 0.92 (Batch 10) over 36 months.*

## ⚙️ Installation
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/yourusername/gas-sensor-drift-compensation.git](https://github.com/Saurabh-html/Saurabh-html-Gas-Sensor-Drift-Compensation-and-Concentration-Quantification/edit/main)
   cd gas-sensor-drift-compensation
   
2. **Installation Dependencies**
pip install -r requirements.txt

**📂 Repository Structure**
.
├── data/                   # Dataset (raw/processed)
├── models/                 # Pretrained models
├── src/                    # Source code
│   ├── preprocess.py       # Data preprocessing
│   ├── train.py            # Model training
│   └── evaluate.py         # Performance evaluation
├── notebooks/              # Jupyter notebooks for EDA
├── media/                  # Visualizations/results
└── requirements.txt        # Dependencies

**Model Deployment**
![Model Deployment](media/model_deployment.png) 

**Output**
![Residual Plot](media/residual_plot.png) 
![Output](media/Output.png) 

**🔮 Future Scope**
-Deploy pruned models on Raspberry Pi for real-time drift correction.
-Integrate LSTM layers to capture temporal drift patterns.
-Extend to multi-sensor fusion networks.

**🤝 Contributing**
Contributions are welcome! Open an issue or submit a PR for:

-Bug fixes
-Performance optimizations
-New features (e.g., hybrid models)

**📜 License**
MIT License. See LICENSE for details.
