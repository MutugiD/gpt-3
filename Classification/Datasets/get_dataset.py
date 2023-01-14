#https://predictivehacks.com/?all-tips=how-to-save-and-load-a-huggingface-dataset
#https://github.com/huggingface/datasets
from datasets import list_datasets, load_dataset
dataset = load_dataset('yelp_polarity')
#dataset.save_to_disk('Datasets/yelp')
for split, data in dataset.items():
    data.to_csv(f"yelp-{split}.csv", index = None)
    
    


# df = pd.read_csv(r'E:\Python Projects\NLP\GPT_samples\Datasets\yelp-train.csv')
# split_dfs = np.array_split(df, 20)
# df1 = split_dfs[0]
# df1 = df1.rename(columns = {'text':'prompt', 'label':'completion'})
# df1.to_csv('E:/Python Projects/NLP/GPT_samples/Datasets/yelp-sentiment.csv', index =0)
# df2 = pd.DataFrame(df1, columns = ['prompt','completion'])

   