from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
digits = load_digits()
x_data = digits.data
y_data = digits.target
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)
y_hat=clf.predict(x_test)
print(y_hat)
print(y_test)
print(accuracy_score(y_test,y_hat))