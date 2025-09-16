def calculation(df):
    df = np.array(df)
    df = df.reshape((3,3))
    mean = []
    var = []
    std = []
    max = []
    min = []
    sum = []
    mean.append(np.mean(df, axis=0).tolist())
    mean.append(np.mean(df, axis=1).tolist())
    mean.append(np.mean(df))
    var.append(np.var(df, axis=0).tolist())
    var.append(np.var(df, axis=1).tolist())
    var.append(np.var(df))
    std.append(np.std(df, axis=0).tolist())
    std.append(np.std(df, axis=1).tolist())
    std.append(np.std(df))
    max.append(np.max(df, axis=0).tolist())
    max.append(np.max(df, axis=1).tolist())
    max.append(np.max(df))
    min.append(np.min(df, axis=0).tolist())
    min.append(np.min(df, axis=1).tolist())
    min.append(np.min(df))
    sum.append(np.sum(df, axis=0).tolist())
    sum.append(np.sum(df, axis=1).tolist())
    sum.append(np.sum(df))
    result = {'mean': mean,
             'variance': var,
             'standard derivation': std,
             'maximum': max,
              'minimum': min,
              'sum': sum
             }
    return result
