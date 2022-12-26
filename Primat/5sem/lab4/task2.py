def accuracy_score(y, y_pred):
    return (y == y_pred).mean()


def recall_score(y, y_pred):
    return (y * y_pred).sum() / y.sum()


def precision_score(y, y_pred):
    return (y * y_pred).sum() / y_pred.sum()


def f_score(y, y_pred):
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    return 2 * precision * recall / (precision + recall)
