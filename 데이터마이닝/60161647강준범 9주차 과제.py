{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "temp=pd.read_csv('C:/User/nba.csv',delimiter=',')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "모듈을 임포트하고 nba파일을 불러온다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Salary</th>\n",
       "      <th>Team</th>\n",
       "      <th>Position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>242</th>\n",
       "      <td>30.0</td>\n",
       "      <td>8193030.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>SF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>243</th>\n",
       "      <td>27.0</td>\n",
       "      <td>306527.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>SF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>244</th>\n",
       "      <td>27.0</td>\n",
       "      <td>6486486.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>PG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>245</th>\n",
       "      <td>30.0</td>\n",
       "      <td>8229375.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>SG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>246</th>\n",
       "      <td>22.0</td>\n",
       "      <td>1242720.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>247</th>\n",
       "      <td>22.0</td>\n",
       "      <td>1646400.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>SF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>248</th>\n",
       "      <td>27.0</td>\n",
       "      <td>200600.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>PG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>249</th>\n",
       "      <td>26.0</td>\n",
       "      <td>15756438.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>SG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>250</th>\n",
       "      <td>22.0</td>\n",
       "      <td>1000000.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>251</th>\n",
       "      <td>30.0</td>\n",
       "      <td>22359364.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>252</th>\n",
       "      <td>24.0</td>\n",
       "      <td>2489530.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>253</th>\n",
       "      <td>23.0</td>\n",
       "      <td>3189794.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>SG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>254</th>\n",
       "      <td>25.0</td>\n",
       "      <td>2288205.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>255</th>\n",
       "      <td>30.0</td>\n",
       "      <td>947276.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>256</th>\n",
       "      <td>38.0</td>\n",
       "      <td>947276.0</td>\n",
       "      <td>Houston Rockets</td>\n",
       "      <td>SG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>227</th>\n",
       "      <td>22.0</td>\n",
       "      <td>1449000.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>SG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>228</th>\n",
       "      <td>31.0</td>\n",
       "      <td>4290000.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>PG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>229</th>\n",
       "      <td>28.0</td>\n",
       "      <td>1100602.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>SF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>230</th>\n",
       "      <td>31.0</td>\n",
       "      <td>3950313.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>PG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>231</th>\n",
       "      <td>33.0</td>\n",
       "      <td>4053446.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>PG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>232</th>\n",
       "      <td>33.0</td>\n",
       "      <td>2085671.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>233</th>\n",
       "      <td>29.0</td>\n",
       "      <td>16407500.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>SG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>234</th>\n",
       "      <td>28.0</td>\n",
       "      <td>1270964.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>235</th>\n",
       "      <td>29.0</td>\n",
       "      <td>525093.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>236</th>\n",
       "      <td>37.0</td>\n",
       "      <td>8333334.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>237</th>\n",
       "      <td>32.0</td>\n",
       "      <td>5200000.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>238</th>\n",
       "      <td>27.0</td>\n",
       "      <td>15361500.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>SF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>239</th>\n",
       "      <td>24.0</td>\n",
       "      <td>845059.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>240</th>\n",
       "      <td>31.0</td>\n",
       "      <td>947276.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>241</th>\n",
       "      <td>31.0</td>\n",
       "      <td>5378974.0</td>\n",
       "      <td>Dallas Mavericks</td>\n",
       "      <td>PG</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Age      Salary              Team Position\n",
       "242  30.0   8193030.0   Houston Rockets       SF\n",
       "243  27.0    306527.0   Houston Rockets       SF\n",
       "244  27.0   6486486.0   Houston Rockets       PG\n",
       "245  30.0   8229375.0   Houston Rockets       SG\n",
       "246  22.0   1242720.0   Houston Rockets       PF\n",
       "247  22.0   1646400.0   Houston Rockets       SF\n",
       "248  27.0    200600.0   Houston Rockets       PG\n",
       "249  26.0  15756438.0   Houston Rockets       SG\n",
       "250  22.0   1000000.0   Houston Rockets       PF\n",
       "251  30.0  22359364.0   Houston Rockets        C\n",
       "252  24.0   2489530.0   Houston Rockets       PF\n",
       "253  23.0   3189794.0   Houston Rockets       SG\n",
       "254  25.0   2288205.0   Houston Rockets       PF\n",
       "255  30.0    947276.0   Houston Rockets        C\n",
       "256  38.0    947276.0   Houston Rockets       SG\n",
       "227  22.0   1449000.0  Dallas Mavericks       SG\n",
       "228  31.0   4290000.0  Dallas Mavericks       PG\n",
       "229  28.0   1100602.0  Dallas Mavericks       SF\n",
       "230  31.0   3950313.0  Dallas Mavericks       PG\n",
       "231  33.0   4053446.0  Dallas Mavericks       PG\n",
       "232  33.0   2085671.0  Dallas Mavericks       PF\n",
       "233  29.0  16407500.0  Dallas Mavericks       SG\n",
       "234  28.0   1270964.0  Dallas Mavericks        C\n",
       "235  29.0    525093.0  Dallas Mavericks        C\n",
       "236  37.0   8333334.0  Dallas Mavericks       PF\n",
       "237  32.0   5200000.0  Dallas Mavericks        C\n",
       "238  27.0  15361500.0  Dallas Mavericks       SF\n",
       "239  24.0    845059.0  Dallas Mavericks       PF\n",
       "240  31.0    947276.0  Dallas Mavericks       PF\n",
       "241  31.0   5378974.0  Dallas Mavericks       PG"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "temp1=pd.concat([temp[temp['Team']=='Houston Rockets'],temp[temp['Team']=='Dallas Mavericks']])\n",
    "temp1=temp1[['Age','Salary','Team','Position']]\n",
    "temp1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Team 칼럼이 'Houston Rockets'인팀과 Dallas Mavericks인 팀을 합쳐서\n",
    "age,salary,team,position만 나타내는 데이터 프레임으로 표현했습니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "g = sns.boxplot(x=\"Age\", y='Salary', hue=\"Position\", data=temp1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "hue를 포지션으로 x축을 나이로 했기 때문에 각 나이마다 그 나이에 속하는 선수들의 포지션에 따라 \n",
    "봉급을 boxplot으로 나타내는 그래프입니다. 각 나이에 포지션이 1명이면 작은 직선이 생기지만 두명이상이되면\n",
    "최대,평균,최소,분위 등의 정보를 줍니다. 이 그림에서는 22살인 PF선수들의 연봉은 거의 비슷해서 박스가 작고\n",
    "24살인 PF도 연봉의 차이가 크지않지만 27살의 SF와 PG는 연봉의 차이가 있어서 박스가 크게 생성된 모습입니다.\n",
    "마지막으로 30살 C의 연봉차이가 컸고 31살 PG들은 거의 연봉차이가 없었습니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\강준범\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\numpy\\linalg\\linalg.py:1965: RuntimeWarning: invalid value encountered in greater\n",
      "  large = s > cutoff\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.JointGrid at 0x25beccc5c10>"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x432 with 3 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.jointplot( data=temp1,x=\"Age\", y=\"Salary\", kind='reg')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "그림을 분석해보면 x축이 나이 y축이 봉급이다. 회귀 분석에 의해 구해진 하늘색 부분에 따르면\n",
    "나이가 많아질수록 조금씩 봉급이 올라간다고 생각할 수 있다.\n",
    "그래프 상단과 오른쪽에 있는 밀도와 히스토그램에 따르면\n",
    "두팀의 구성원중 32살이 가장 많았고 그다음 22,24살 순이였다.\n",
    "봉급은 보통 낮은 사람이 대부분이고 높은사람은 거의 없었다.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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nTpl8uTJ+drXvpZly5ale/fuSZLPfvazGT58+Aav2WbgPmHChNx4443/8BgAAAAAAGyK1Wua0q1LTbutN3/+/Nx///257bbb0rVr16xYsSJr1qxJknzta1/LAQccsFHXbRG4r169Oi+//HJWrlyZv/3tb6lWq0mSF198McuWLduoiwAAAAAAQFu6danJwWfcVGy9h//r39d7fvny5endu3e6du2aJNlpp52KXLdF4H7LLbfkxhtvzLJlyzJmzJjmwL1Xr1755Cc/WeSiAAAAAADQUQ477LBce+21GTZsWD7wgQ/kqKOOyvve974kyemnn968pcz//M//pHfv3hu8bovAfcKECZkwYUK+//3v59hjjy1UPgAAAAAAbBl69uyZadOm5Te/+U0eeuihnHLKKTnttNOSFN5S5jXHHntsfvvb3+bpp59OU1NT8/HRo0dv1IUAAAAAAGBLUVNTk0GDBmXQoEHp379/pk+fvslrthm4n3HGGXnyySez7777pqbm/zaXr1QqAncAAAAAALZqf/nLX9KpU6e8853vTJIsWrQou+66axYvXrxJ67YZuD/yyCO58847U6lUNukCAAAAAACwJfn73/+eKVOmZNWqVampqcmee+6ZyZMn5/Of//wmrdtm4N6vX78sX748tbW1m3QBAAAAAABYn9VrmvLwf/170fW6dalp8/z++++fW265pcXx73//+5t03TYD95UrV2bEiBF5z3veky5dujQf/+Y3v7lJFwQAAAAAgNdbXzi+Jay3odoM3E8++eT2rAMAAAAAALZqbQbu73vf+9qzDgAAAAAA2Kq1Gbi/973vbf6FqWvWrEljY2N69OiR3/72t+1WHAAAAAAAbC3aDNznz5+/zuv77rsvCxcu3OwFAQAAAADA1qjThg484ogj8uCDD27OWgAAAAAAYKvV5hPus2bNav7z2rVr88gjjzRvMQMAAAAAAFuz/fbbL/37909TU1P69u2bSy+9ND169Mizzz6biy++OAsWLMhb3/rWdOnSJccdd1yGDh36D9dsM3D/+c9/3vznmpqa7Lbbbvnv//7vMn8TAAAAAAD4f6qNq1Pp3K1d1+vevXtmzJiRJDnttNNyyy235D/+4z9y4oknZvTo0bn88suTJE8//XTmzJmzQddtM3C/+OKLN7T2ZmeffXbuv//+7Lzzzpk5c2aL8w899FA+97nPZffdd0+SDB06NCeddNKbvg4AAAAAANuOSudueWLyAcXW+6fzfv+mxg8cODCPPfZYHnzwwXTp0iXjxo1rPrfbbrvl2GOP3aB12gzcly5dmgsuuCC//e1vU6lUcvDBB+fcc89Nnz592lxszJgxGT9+fM4888z1Fn799ddvUHEAAAAAALA5NTY2Zu7cufnQhz6UxYsX593vfvdGr9XmL009++yzM2TIkDzwwAOZO3duPvzhD+fss89e72KHHHJI3vrWt250MQAAAAAA0B5eeeWV1NXVZezYsdl1111zzDHHtBjz1a9+NUcffXTGjh27QWu2+YT7ihUr1llkzJgxufHGGzei7HUtWLAgRx99dGpra3PmmWemX79+m7wmAAAAAAC8Ga/fw/01/fr1y6xZs5pff+UrX8mKFStaDeNb0+YT7r17986MGTPS1NSUpqamzJgxIzvuuOPGVf7/DBgwIHPmzMnPfvazHHvssTnxxBM3aT0AAAAAACjl/e9/f1avXp2bb765+dgrr7yywfPbDNwvuuii3HXXXTnssMPywQ9+MPfcc89G/SLV1+vVq1d69uyZJBk8eHAaGxuzYsWKTVoTAAAAAABKqFQqufbaa/PrX/86Q4YMyTHHHJMzzzwzp59++gbNb3NLmauuuiqXXnpp857szz//fC699NJNCt2XL1+et73tbalUKlm4cGHWrl2b3r17b/R6AAAAAABs/aqNq/NP5/2+6HqVzt3WO2b+/PmtHq+trc2VV165UddtM3B/7LHH1vkFqDvuuGMWLVq03sVOPfXUzJs3LytXrszhhx+ek08+OY2NjUmScePG5Z577snUqVNTU1OT7t2754orrkilUtmowgEAAAAA2Db8o3C8o9fbUG0G7mvXrs3f/va3dZ5wb2pqWu9iV1xxxXrPjx8/PuPHj9+IMgEAAAAAYMvWZuD+qU99Kp/4xCcybNiwVCqV3HXXXTnhhBPaszYAAAAAANhqtBm4jx49Ovvvv38efPDBVKvVXHPNNdl7773bszYAAAAAANhqtBm4J8nee+8tZAcAAAAAgA3QqaMLAAAAAACAbcF6n3AHAAAAAIBt0XXXXZeZM2emU6dO6dSpUyZPnpwBAwbk6quvzt13350ePXokSYYPH57PfvazG7SmwB0AAAAAgA61unF1unXu1m7rzZ8/P/fff39uu+22dO3aNStWrMiaNWvy9a9/Pc8++2xuv/32dOvWLS+++GK+973vbfB1Be4AAAAAAHSobp275bBvHFZsvV+c/Iv1nl++fHl69+6drl27Jkl22mmnvPzyy7n11lsze/bsdOv2f2F9r169cvLJJ2/wde3hDgAAAADAduWwww7LM888k2HDhuX888/PvHnz8r//+795xzvekV69em30ugJ3AAAAAAC2Kz179sy0adMyefLk7LTTTjnllFMyb968dcb89Kc/TV1dXQYPHpxnnnlmg9a1pQwAAAAAANudmpqaDBo0KIMGDUr//v3zox/9KM8880xefPHF9OrVK2PHjs3YsWMzcuTINDU1bdCannAHAAAAAGC78pe//CVLlixpfr1o0aLstddeGTt2bC644IKsXr06SdLU1JQ1a9Zs8LqecAcAAAAAYLvy97//PVOmTMmqVatSU1OTPffcM5MnT84OO+yQq666KiNHjkzPnj3TvXv3jB49OrW1tRu0rsAdAAAAAIAOtbpxdX5x8i+Krtetc7c2z++///655ZZbWj13+umn5/TTT9+o69pSBgAAAACADrW+cHxLWG9DCdwBAAAAAKAAgTsAAAAAABQgcAcAAAAAgAIE7gAAAAAAUIDAHQAAAAAACujc0QUAAAAAAEB722+//dK/f/80NTWlb9++ufTSS9OjR4/m46+59tprs/vuu2/QmgJ3AAAAAAA61NrVq9OpW7d2Xa979+6ZMWNGkuS0007LLbfckokTJ65z/M0SuAMAAAAA0KE6deuW+sMHF1tv8Nz6NzV+4MCBeeyxxzb5ugJ3AAAAAAC2W42NjZk7d24+9KEPJUleeeWV1NXVJUl23333XHvttRu8lsAdAAAAAIDtzuuD9YEDB+aYY45JElvKAAAAAADAm7EpwXpbOhVdDQAAAAAAtlMCdwAAAAAAKMCWMgAAAAAAdKi1q1dn8Nz6out16tZtvWPmz5//po5vCE+4AwAAAADQof5RON7R623wdTvkqgAAAAAAsI0RuAMAAAAAQAECdwAAAAAAKEDgDgAAAAAABQjcAQAAAACggM4dXQAAAAAAALS35cuX56KLLsrvf//7dO3aNbvttlvOOeec7LXXXhu9psAdAAAAAIAO1bimKZ271LTbetVqNSeddFJGjx6dK6+8MkmyaNGiPPfccwJ3AAAAAAC2Xp271OSa024vtt5J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jzzySLVarVZfeOGF6pFHHlldvHhx9YEHHqiuWbOmWq1Wq5dddln1sssuazG3sbGx+pGPfKT6xBNPVFevXl0dNWpUdfHixe1a/7amrX688MILzWNuvPHG6pe//OUWc/WjrLZ6Ua1Wq3/961+rn/rUp6r/8i//Un3uuedazNWL8trqx9VXX1399re/vd65+lFWW7341a9+VZ0wYUJ19erV1Wq1Wn322WdbzNWL8tb3WfWaiy++uPqNb3yjxVz9KKutXkycOLF6//33V6vVavX++++vjh8/vsVcvSivrX6MGTOm+tBDD1Wr1Wr11ltvrV555ZUt5upHWWvXrq2++OKL1Wq1Wn311VerxxxzTHX+/PnVSy+9tHr99ddXq9Vq9frrr/d9ox201Ys//elP1T//+c/V8ePHVxcuXNjqXL0or61++C7e/trqhe/hHaOtfrye+9v20VYv3N9u+zzhvolqa2szYMCAJEmvXr3St2/fNDQ05IMf/GA6d+6cJDnooIOydOnSFnMXLlyYPffcM3vssUe6du2aESNGZPbs2e1a/7amrX706tWreczLL7+cSqXSYq5+lNVWL5Lk4osvzhlnnNFqHxK92BzW149/RD/KaqsXU6dOzfHHH5+uXbsmSXbeeecWc/WivH/03qhWq7nrrrsycuTIFnP1o6y2elGpVPLSSy8lSV544YXU1ta2mKsX5bXVj8cffzyHHHJIkuSwww7LrFmzWszVj7IqlUp69uyZJGlsbExjY2MqlUpmz56d0aNHJ0lGjx6d++67r8VcvSirrV68613vSt++fdc7Vy/Ka6sfvou3v7Z64Xt4x2irH69xf9t+2uqF+9ttn8C9oKeeeiqLFi3KgQceuM7xn/70pzn88MNbjG9oaEifPn2aX++yyy4bHIDxj72xH1deeWUGDx6c22+/PZ///OdbjNePzef1vZg9e3Zqa2uz7777tjleLzavN743fvjDH2bUqFE5++yzW/1xdP3YfF7fiyVLluQ3v/lNPvaxj2X8+PGt/lihXmxerf07/pvf/CY777xz3vnOd7YYrx+bz+t7cc455+Syyy7L4MGDc+mll+bUU09tMV4vNq/X96N///7NX/buvvvuPPPMMy3G60d5TU1Nqaury6GHHppDDz00Bx54YJ577rnmL+i1tbWtbtOnF+W11osNoRebxz/qh+/i7aetXvge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\n",
      "text/plain": [
       "<Figure size 1490.38x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "with sns.axes_style('white'):\n",
    "    g = sns.catplot(x=\"Age\", data=temp1, aspect=4.0, kind='count',hue='Position')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "나이에 따른 포지션별 사람의 수를 세주는 그래프이다 예를들어 22살 PF는 2명 SF,SG는 한명씩이다\n",
    "24살에는 PF만 2명,27살에는 SF,PG 2명씩있고 31살에는 PG가 3명이나 있는 그림이다\n",
    "어느 나이에 어느 포지션이 가장 많고 몇명인지 잘 알 수 있다."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
