{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "df=pd.read_csv('C:/User/nba.csv',delimiter=',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
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
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Position</th>\n",
       "      <th>Team</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">C</th>\n",
       "      <th>Atlanta Hawks</th>\n",
       "      <td>28.333333</td>\n",
       "      <td>7.585417e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Boston Celtics</th>\n",
       "      <td>25.000000</td>\n",
       "      <td>2.450465e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Brooklyn Nets</th>\n",
       "      <td>27.000000</td>\n",
       "      <td>1.031814e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Charlotte Hornets</th>\n",
       "      <td>25.666667</td>\n",
       "      <td>6.772240e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Chicago Bulls</th>\n",
       "      <td>33.000000</td>\n",
       "      <td>1.042438e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">SG</th>\n",
       "      <th>Sacramento Kings</th>\n",
       "      <td>26.250000</td>\n",
       "      <td>2.794976e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>San Antonio Spurs</th>\n",
       "      <td>31.250000</td>\n",
       "      <td>3.384923e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Toronto Raptors</th>\n",
       "      <td>24.500000</td>\n",
       "      <td>5.350000e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Utah Jazz</th>\n",
       "      <td>23.500000</td>\n",
       "      <td>5.405962e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Washington Wizards</th>\n",
       "      <td>27.250000</td>\n",
       "      <td>2.839248e+06</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>149 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                   Age        Salary\n",
       "Position Team                                       \n",
       "C        Atlanta Hawks       28.333333  7.585417e+06\n",
       "         Boston Celtics      25.000000  2.450465e+06\n",
       "         Brooklyn Nets       27.000000  1.031814e+07\n",
       "         Charlotte Hornets   25.666667  6.772240e+06\n",
       "         Chicago Bulls       33.000000  1.042438e+07\n",
       "...                                ...           ...\n",
       "SG       Sacramento Kings    26.250000  2.794976e+06\n",
       "         San Antonio Spurs   31.250000  3.384923e+06\n",
       "         Toronto Raptors     24.500000  5.350000e+06\n",
       "         Utah Jazz           23.500000  5.405962e+06\n",
       "         Washington Wizards  27.250000  2.839248e+06\n",
       "\n",
       "[149 rows x 2 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "temp=df.groupby(['Position','Team'])[['Age','Salary']].mean()\n",
    "temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 5 artists>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXQAAAEDCAYAAAAlRP8qAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/d3fzzAAAACXBIWXMAAAsTAAALEwEAmpwYAAAODElEQVR4nO3df6jd9X3H8edrJm1XFBzLpUpMjGyZo3bzxzJ/rLC5wkCdLBtzECd1c6WZYkcFxyYt2MHG2P7RobGGgLYVnI7+EmHpuoIVLdRiEqImijZztQYDRqXRTK2LvPfH/aY73HvuPecm59xz7yfPB1w85/v93HPfX3J5eu73fs+5qSokScvfz016AEnSaBh0SWqEQZekRhh0SWqEQZekRhh0SWrERIOe5N4krybZM8Ta25Ps7j5eSPKTRRhRkpaNTPI69CS/DRwG7quqjy3g8/4KOL+q/mJsw0nSMjPRZ+hV9RjwRu+2JL+U5D+S7EzyeJJf7fOpVwMPLMqQkrRMrJj0AH1sA66vqh8muQj4IvCJozuTnAmcBTwyofkkaUlaUkFPcjLwW8BXkxzd/MEZyzYBX6uq9xdzNkla6pZU0Jk+BfSTqjpvnjWbgBsXZxxJWj6W1GWLVfUm8N9J/gQg0849uj/J2cAvAN+f0IiStGRN+rLFB5iO89lJ9if5FHAN8KkkTwF7gY09n3I18GD5FpGSNMtEL1uUJI3OkjrlIkk6dhP7peiqVatq3bp1k/rykrQs7dy587Wqmuq3b2JBX7duHTt27JjUl5ekZSnJS3Pt85SLJDXCoEtSIwy6JDXCoEtSIwy6JDXCoEtSIwYGPcmaJN9N8lySvUk+22fNpUkO9fxFoVvHM64kaS7DXId+BLi5qnYlOQXYmeQ7VfXsjHWPV9WVox9RkjSMgc/Qq+pAVe3qbr8FPAesHvdgkqSFWdArRZOsA84HftBn9yXdOyS+Avx1Ve3t8/mbgc0Aa9euXfCw0olu3S3/PukRRuJH//T7kx6hSUP/UrT7a0JfB27q3re81y7gzKo6F7gTeKjfY1TVtqraUFUbpqb6vhWBJOkYDRX0JCuZjvn9VfWNmfur6s2qOtzd3g6sTLJqpJNKkuY1zFUuAe4Bnquq2+ZYc1q3jiQXdo/7+igHlSTNb5hz6B8HPgk8k2R3t+1zwFqAqtoKXAXckOQI8A6wyb8qJEmLa2DQq+p7QAas2QJsGdVQkqSF85WiktQIgy5JjTDoktQIgy5JjTDoktQIgy5JjTDoktQIgy5JjTDoktQIgy5JjTDoktQIgy5JjTDoktQIgy5JjTDoktQIgy5JjRjmLxYtOa385XPwr59LGp1lGfQTnf9Dk9SPp1wkqREGXZIaYdAlqREGXZIaYdAlqRFe5aJlxSt8pLn5DF2SGmHQJakRBl2SGmHQJakRBl2SGmHQJakRBl2SGmHQJakRA4OeZE2S7yZ5LsneJJ/tsyZJ7kiyL8nTSS4Yz7iSpLkM80rRI8DNVbUrySnAziTfqapne9ZcDqzvPi4C7u7+K0laJAOfoVfVgara1d1+C3gOWD1j2Ubgvpr2BHBqktNHPq0kaU4Lei+XJOuA84EfzNi1Gni55/7+btuBGZ+/GdgMsHbt2gWOKulE5vv4DDb0L0WTnAx8Hbipqt6cubvPp9SsDVXbqmpDVW2Ymppa2KSSpHkNFfQkK5mO+f1V9Y0+S/YDa3runwG8cvzjSZKGNcxVLgHuAZ6rqtvmWPYwcG13tcvFwKGqOjDHWknSGAxzDv3jwCeBZ5Ls7rZ9DlgLUFVbge3AFcA+4G3gupFPKkma18CgV9X36H+OvHdNATeOaihJ0sL5SlFJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGGHRJaoRBl6RGDAx6knuTvJpkzxz7L01yKMnu7uPW0Y8pSRpkxRBrvgxsAe6bZ83jVXXlSCaSJB2Tgc/Qq+ox4I1FmEWSdBxGdQ79kiRPJflWknNG9JiSpAUY5pTLILuAM6vqcJIrgIeA9f0WJtkMbAZYu3btCL60JOmo436GXlVvVtXh7vZ2YGWSVXOs3VZVG6pqw9TU1PF+aUlSj+MOepLTkqS7fWH3mK8f7+NKkhZm4CmXJA8AlwKrkuwHvgCsBKiqrcBVwA1JjgDvAJuqqsY2sSSpr4FBr6qrB+zfwvRljZKkCfKVopLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUiIFBT3JvkleT7Jljf5LckWRfkqeTXDD6MSVJgwzzDP3LwGXz7L8cWN99bAbuPv6xJEkLNTDoVfUY8MY8SzYC99W0J4BTk5w+qgElScMZxTn01cDLPff3d9tmSbI5yY4kOw4ePDiCLy1JOmoUQU+fbdVvYVVtq6oNVbVhampqBF9aknTUKIK+H1jTc/8M4JURPK4kaQFGEfSHgWu7q10uBg5V1YERPK4kaQFWDFqQ5AHgUmBVkv3AF4CVAFW1FdgOXAHsA94GrhvXsJKkuQ0MelVdPWB/ATeObCJJ0jHxlaKS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNMOiS1AiDLkmNGCroSS5L8nySfUlu6bP/0iSHkuzuPm4d/aiSpPmsGLQgyUnAXcDvAfuBJ5M8XFXPzlj6eFVdOYYZJUlDGOYZ+oXAvqp6sareAx4ENo53LEnSQg0T9NXAyz3393fbZrokyVNJvpXknH4PlGRzkh1Jdhw8ePAYxpUkzWWYoKfPtppxfxdwZlWdC9wJPNTvgapqW1VtqKoNU1NTCxpUkjS/YYK+H1jTc/8M4JXeBVX1ZlUd7m5vB1YmWTWyKSVJAw0T9CeB9UnOSvIBYBPwcO+CJKclSXf7wu5xXx/1sJKkuQ28yqWqjiT5DPBt4CTg3qram+T6bv9W4CrghiRHgHeATVU187SMJGmMBgYdfnYaZfuMbVt7bm8Btox2NEnSQvhKUUlqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqhEGXpEYYdElqxFBBT3JZkueT7EtyS5/9SXJHt//pJBeMflRJ0nwGBj3JScBdwOXAR4Grk3x0xrLLgfXdx2bg7hHPKUkaYJhn6BcC+6rqxap6D3gQ2DhjzUbgvpr2BHBqktNHPKskaR4rhlizGni55/5+4KIh1qwGDvQuSrKZ6WfwAIeTPL+gaRffKuC1cX6B/PM4H/24jP3Y4cQ+fo99SVoO3/dnzrVjmKCnz7Y6hjVU1TZg2xBfc0lIsqOqNkx6jkk4kY8dTuzj99iX77EPc8plP7Cm5/4ZwCvHsEaSNEbDBP1JYH2Ss5J8ANgEPDxjzcPAtd3VLhcDh6rqwMwHkiSNz8BTLlV1JMlngG8DJwH3VtXeJNd3+7cC24ErgH3A28B14xt5US2b00NjcCIfO5zYx++xL1OpmnWqW5K0DPlKUUlqhEGXpEYY9D6SnJbkwST/leTZJNuT/Mqk5xqXJO8n2Z1kT5KvJvnwjO1HP9ZNeNSRm+fYP5LkX5O8mGRnku8n+aNJzzsOST6fZG/3th27k1yU5NHu7T6O/ttfNek5R22O416R5B+T/LDn2D8/6VmHNcx16CeUJAG+CXylqjZ1284DPgK8MMHRxumdqjoPIMn9wPXAbb3bGzbr2JPcDjzE9PfAn3b7zgT+YFJDjkuSS4ArgQuq6qdJVgEf6HZfU1U7Jjfd+Mxz3P8AnAb8WlW9m+QU4OYJjrogBn223wX+t7t6B4Cq2j25cRbd48CvT3qICTl67J8A3pvxPfAScOekBhuj04HXquqnAFX1GsD085qmzTru7qezTwPrqurdbvtbwN9NbMoF8pTLbB8Ddk56iElIsoLpN1p7ptv08z0/dn5zgqON3YxjPwfYNdmJFs1/AmuSvJDki0l+p2ff/T3//r84qQHHpN9x/zLw4y7iy5JBF3ThBnYAPwbu6ba/U1XndR9Nnj9m7mP/mSR3JXkqyZOLPdy4VdVh4DeYfo+lg8C/Jfnzbvc1Pf/+r09qxnHod9zApb1rklzX/c/s5SRrZj/K0uMpl9n2As39AmiAE+Fc+VxmHXuSvcAfH71fVTd251ibPJ9cVe8DjwKPJnkG+LPJTrQ4+hz3XwJrk5xSVW9V1ZeALyXZw/SLKpc8n6HP9gjwwSSfProhyW/O+FFUbXsE+FCSG3q2fXhSw4xTkrOTrO/ZdB7w0oTGWTRzHPfzTP+EtiXJh7p1J/H/vyRe8nyGPkNVVXd52r9k+q8zvQv8CLhpknNp8XTfA38I3J7kb5j+kfx/gL+d6GDjcTJwZ5JTgSNMv33HZuBrkxxqEcx13IeAvwf2JHkLeAf4CsvkzQZ96b8kNcJTLpLUCIMuSY0w6JLUCIMuSY0w6JLUCIMuSY0w6JLUiP8DpBOFFTVHaXcAAAAASUVORK5CYII=\n",
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
    "f=lambda x:x.max()\n",
    "gp_by_pos=df.groupby('Position')\n",
    "plt.bar(gp_by_pos.apply(f)['Salary'].index,gp_by_pos.apply(f)['Salary'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1296x432 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(18,6))\n",
    "plt.subplot(2,1,1)\n",
    "gp_by_team=df.groupby('Team')\n",
    "change=list(gp_by_team['Salary'].apply(f).index)\n",
    "for i in range(len(change)):\n",
    "    a=change[i].split(' ')\n",
    "    b=a[0][0]+a[1][0]\n",
    "    change[i]=b\n",
    "plt.title('Maxium salary for each tem')\n",
    "plt.bar(change,gp_by_team['Salary'].apply(f))\n",
    "plt.subplot(2,1,2)\n",
    "plt.title('Maxium age for each tem')\n",
    "plt.bar(change,gp_by_team['Age'].apply(f))\n",
    "plt.subplots_adjust(hspace=0.4, wspace=0.4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
