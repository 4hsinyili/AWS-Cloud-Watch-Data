# How to get or put AWS Cloud Watch data using boto3?
這是我測試從 AWS Cloudwatch Metrics 取跟放資料的程式，有需要的人可以自行取用，[官方文檔](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html?highlight=cloudwatch)在這。使用之前請先參考[這裏](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)作前置作業。但除非特殊情況，建議直接看 Cloud Watch 頁面的圖表就好了，因為從 Cloud Watch 取用資料有諸多限制，詳細請看以下紀錄：

## 讀取資料會有資料量的限制
例如我將 period 設定為 300 ，那麼 cloudwatch 就會將一天切割為 300 秒為單位的時段（共 288 個時段），不論該時段內有沒有找到資料，都會算一個資料點，而回傳的資料點上限是 1440 個，所以不適合取大範圍且時段切分細的資料

## 資料存取會有延遲
在取跟放資料時都要記得，他會有最多五分鐘的延遲，這項延遲應該是可以調整的，但我沒有深入研究

## 資料大小有限制
如果要放資料的話，資料的大小有限制，建議是放秒數、爬到的資料數量，這種 int 類型的資料

## 自創資料分類
如果要放資料的話，最好是自創一個 Namespace，自由度比較高，也不怕污染到原本的資料；應該說不自創 Namespace 的話，也不確定能不能放進去，我試著放過，雖然程式沒有有報錯，也有回應 200，但資料一直沒有出現

## 自創資料分類會有延遲
自創 Namespace 跟 Metric 時，會有最多 15 分鐘的建立時間
