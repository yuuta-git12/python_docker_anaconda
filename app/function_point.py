# ファンクションポイントの重み（単純、中程度、複雑）
weights = {
    'EI': [3, 4, 6],  # 外部入力
    'EO': [4, 5, 7],  # 外部出力
    'EQ': [3, 4, 6],  # 外部参照
    'ILF': [7, 10, 15],  # 内部論理ファイル
    'EIF': [5, 7, 10]  # 外部インターフェースファイル
}

# システムの機能に対する入力 (単純: 0, 中程度: 1, 複雑: 2)
functions = {
    'EI': [5, 3, 2],  # 単純な外部入力が5つ、中程度が3つ、複雑が2つ
    'EO': [2, 4, 1],  # 単純な外部出力が2つ、中程度が4つ、複雑が1つ
    'EQ': [3, 1, 0],  # 単純な外部参照が3つ、中程度が1つ、複雑が0つ
    'ILF': [2, 1, 1],  # 単純な内部論理ファイルが2つ、中程度が1つ、複雑が1つ
    'EIF': [1, 0, 1]   # 単純な外部インターフェースファイルが1つ、中程度が0つ、複雑が1つ
}


# 各機能に対するFPの計算
def calculate_fp(functions, weights):
    total_fp = 0
    for function_type, counts in functions.items():
        for complexity, count in enumerate(counts):
            total_fp += count * weights[function_type][complexity]
    return total_fp


# 未調整のFPを計算
unadjusted_fp = calculate_fp(functions, weights)
print(f"未調整のファンクションポイント: {unadjusted_fp}")

# 調整ファクター(補正係数)の適用 (例として0.65から1.35の範囲で調整)
adjustment_factor = 1.2  # 調整ファクター（仮定）
adjusted_fp = unadjusted_fp * adjustment_factor
print(f"調整後のファンクションポイント: {adjusted_fp}")


# チームの経験・プロジェクトの難易度によって動的に生産性を設定する関数
def set_productivity(team_experience, project_complexity):
    # チームの経験が高ければ生産性は向上
    if team_experience == 'high':
        base_productivity = 3  # 1FPあたりの工数(高いスキルの場合)
    elif team_experience == 'medium':
        base_productivity = 5  # 標準的な工数
    else:
        base_productivity = 7  # 経験が浅い場合の工数
    # プロジェクトの難易度によって生産性を調整
    if project_complexity == 'high':
        return base_productivity * 1.5  # 複雑なプロジェクトは工数が増加
    elif project_complexity == 'low':
        return base_productivity * 0.8  # 簡単なプロジェクトは工数が減少
    else:
        return base_productivity  # 標準的なプロジェクト


# チームの経験とプロジェクトの難易度を入力
team_experience = 'medium'  # チームのスキルレベル(high,medium,low)
project_complexity = 'high'  # プロジェクトの難易度(high,medium,low)

# 動的に生産性を設定
# 1ファンクションポイントあたりの工数(人日/FP)
productivity_per_fp = set_productivity(team_experience, project_complexity)

print(f"生産性(人日/FP) : {productivity_per_fp}")

# 総工数の計算
total_effort = adjusted_fp * productivity_per_fp
print(f"総工数（人日）: {total_effort}")

# さらに、コストの計算も可能
# 1人日あたりの単価（例: 10万円/人日）
cost_per_day = 10  # 万円/人日
total_cost = total_effort * cost_per_day
print(f"総コスト（万円）: {total_cost}")
