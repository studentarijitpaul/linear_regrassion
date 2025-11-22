class maralr:

    def __init__(self):
        self.coefficient = None
        self.intercept = None

    def fit(self, X, y):
        n_samples = len(X)
        x_mean = sum(X) / n_samples
        y_mean = sum(y) / n_samples

        numerator = sum((X[i] - x_mean) * (y[i] - y_mean) for i in range(n_samples))
        denominator = sum((X[i] - x_mean) ** 2 for i in range(n_samples))

        self.coefficient = numerator / denominator
        self.intercept = y_mean - self.coefficient * x_mean

    def predict(self, X):
        return [self.coefficient * x + self.intercept for x in X]
# Simple Linear Regression Implementation       
if __name__ == "__main__":
    # Example usage
    X = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    model = maralr()
    model.fit(X, y)
    predictions = model.predict(X)

    print("Coefficient:", model.coefficient)
    print("Intercept:", model.intercept)
    print("Predictions:", predictions)
# Simple Linear Regression Implementation
