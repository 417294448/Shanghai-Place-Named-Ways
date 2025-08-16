#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
上海地名道路多维度数据分析（无依赖版本）
"""

import re
from collections import Counter, defaultdict

def load_data():
    """从markdown文件加载数据"""
    data = []
    file_path = '/Users/xiaoshuang/Documents/cursor_code/Shanghai-Place-Named-Ways/by_district/all.md'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 解析表格数据
    lines = content.split('\n')
    for line in lines:
        if line.startswith('|') and '区域' not in line and '---' not in line and len(line.strip()) > 5:
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 5:
                data.append({
                    '区域': parts[0],
                    '路名': parts[1], 
                    '省份': parts[2],
                    '地名': parts[3],
                    '相关信息': parts[4]
                })
    
    return data

def basic_analysis(data):
    """基础统计分析"""
    print("=" * 50)
    print("基础统计信息")
    print("=" * 50)
    print(f"道路总数: {len(data)}")
    
    # 统计区域
    districts = [item['区域'] for item in data]
    district_counts = Counter(districts)
    print(f"涉及区域: {len(district_counts)}个")
    
    # 统计省份
    provinces = [item['省份'] for item in data]
    province_counts = Counter(provinces)
    print(f"涉及省份: {len(province_counts)}个")
    
    print("\n各区道路数量排名:")
    for i, (district, count) in enumerate(district_counts.most_common(), 1):
        print(f"{i:2d}. {district:<8}: {count:2d}条")
    
    print("\n各省份使用频率排名:")
    for i, (province, count) in enumerate(province_counts.most_common(15), 1):
        print(f"{i:2d}. {province:<8}: {count:2d}次")
    
    return district_counts, province_counts

def geographical_analysis(data):
    """地理分布分析"""
    print("\n" + "=" * 50)
    print("地理分布分析")
    print("=" * 50)
    
    # 按地理区域分组
    regions = {
        '华北': ['北京', '天津', '河北', '山西', '内蒙古'],
        '东北': ['辽宁', '吉林', '黑龙江'],
        '华东': ['江苏', '浙江', '安徽', '福建', '江西', '山东'],
        '华中': ['河南', '湖北', '湖南'],
        '华南': ['广东', '广西', '海南'],
        '西南': ['四川', '贵州', '云南', '西藏'],
        '西北': ['陕西', '甘肃', '青海', '宁夏', '新疆'],
        '港澳台': ['香港', '澳门', '台湾']
    }
    
    province_counts = Counter([item['省份'] for item in data])
    region_counts = {}
    
    for region, provinces in regions.items():
        count = sum(province_counts.get(p, 0) for p in provinces)
        region_counts[region] = count
    
    print("各地理区域道路数量:")
    sorted_regions = sorted(region_counts.items(), key=lambda x: x[1], reverse=True)
    for i, (region, count) in enumerate(sorted_regions, 1):
        percentage = count / len(data) * 100
        print(f"{i}. {region:<6}: {count:3d}条 ({percentage:5.1f}%)")
    
    return region_counts

def keyword_analysis(data):
    """关键词分析"""
    print("\n" + "=" * 50)
    print("关键词分析")
    print("=" * 50)
    
    # 提取相关信息中的关键词
    all_info = ' '.join([item['相关信息'] for item in data if item['相关信息']])
    
    keywords = {
        '商业相关': ['商业', '商圈', '商店', '购物', '商场', '市场'],
        '交通设施': ['地铁', '公交', '交通', '道路', '桥梁', '站点'],
        '居住区域': ['居民区', '住宅', '小区', '社区', '新村'],
        '教育文化': ['学校', '大学', '教育', '校园', '文化', '博物馆'],
        '工业园区': ['工业', '企业', '厂区', '开发区', '园区'],
        '休闲娱乐': ['公园', '广场', '体育', '娱乐'],
        '餐饮美食': ['餐饮', '美食', '饭店', '餐厅', '小吃']
    }
    
    keyword_counts = {}
    for category, words in keywords.items():
        count = sum(all_info.count(word) for word in words)
        keyword_counts[category] = count
    
    print("功能区域关键词统计:")
    sorted_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)
    for i, (category, count) in enumerate(sorted_keywords, 1):
        print(f"{i}. {category:<8}: {count:3d}次")
    
    return keyword_counts

def naming_pattern_analysis(data):
    """命名模式分析"""
    print("\n" + "=" * 50)
    print("命名模式分析")
    print("=" * 50)
    
    # 1. 道路类型分析
    road_types = Counter()
    for item in data:
        road = item['路名']
        if '路' in road:
            road_types['路'] += 1
        elif '街' in road:
            road_types['街'] += 1
        elif '道' in road:
            road_types['道'] += 1
        else:
            road_types['其他'] += 1
    
    print("道路类型分布:")
    for road_type, count in road_types.most_common():
        percentage = count / len(data) * 100
        print(f"  {road_type}: {count:3d}条 ({percentage:5.1f}%)")
    
    # 2. 路名长度分析
    name_lengths = [len(item['路名']) for item in data]
    avg_length = sum(name_lengths) / len(name_lengths)
    min_length = min(name_lengths)
    max_length = max(name_lengths)
    
    print(f"\n路名长度统计:")
    print(f"  平均长度: {avg_length:.1f}字符")
    print(f"  最短: {min_length}字符")
    print(f"  最长: {max_length}字符")
    
    # 3. 地名类型分析
    print("\n地名类型分析:")
    geo_types = {
        '山脉地形': ['山', '岭', '峰', '岗', '坡'],
        '水系河流': ['江', '河', '湖', '海', '池', '泉'],
        '行政区划': ['市', '县', '区', '镇', '乡'],
        '方位词汇': ['东', '西', '南', '北', '中']
    }
    
    for category, keywords in geo_types.items():
        count = 0
        for item in data:
            for keyword in keywords:
                if keyword in item['地名']:
                    count += 1
                    break
        percentage = count / len(data) * 100
        print(f"  {category}: {count:3d}个 ({percentage:5.1f}%)")

def district_province_correlation(data):
    """区域-省份关联分析"""
    print("\n" + "=" * 50)
    print("区域-省份关联分析")
    print("=" * 50)
    
    # 创建区域-省份映射
    district_province = defaultdict(lambda: defaultdict(int))
    for item in data:
        district_province[item['区域']][item['省份']] += 1
    
    # 找出每个区域最常用的省份
    print("各区域最偏好的省份:")
    for district in sorted(district_province.keys()):
        province_counts = district_province[district]
        top_province = max(province_counts.items(), key=lambda x: x[1])
        total = sum(province_counts.values())
        percentage = top_province[1] / total * 100
        print(f"  {district:<8}: {top_province[0]} ({top_province[1]}/{total}, {percentage:.1f}%)")
    
    # 找出每个省份最集中的区域
    province_district = defaultdict(lambda: defaultdict(int))
    for item in data:
        province_district[item['省份']][item['区域']] += 1
    
    print("\n各省份最集中的区域:")
    province_counts = Counter([item['省份'] for item in data])
    for province, _ in province_counts.most_common(10):
        district_counts = province_district[province]
        if district_counts:
            top_district = max(district_counts.items(), key=lambda x: x[1])
            total = sum(district_counts.values())
            percentage = top_district[1] / total * 100
            print(f"  {province:<8}: {top_district[0]} ({top_district[1]}/{total}, {percentage:.1f}%)")

def create_summary_report(data, district_counts, province_counts, region_counts):
    """生成分析摘要报告"""
    print("\n" + "=" * 50)
    print("分析摘要报告")
    print("=" * 50)
    
    print("核心发现:")
    top_district = district_counts.most_common(1)[0]
    top_province = province_counts.most_common(1)[0]
    
    print(f"1. 道路分布最多的区域: {top_district[0]} ({top_district[1]}条)")
    print(f"2. 使用频率最高的省份: {top_province[0]} ({top_province[1]}次)")
    print(f"3. 平均每个区域有道路: {len(data) / len(district_counts):.1f}条")
    print(f"4. 平均每个省份被使用: {len(data) / len(province_counts):.1f}次")
    
    # 地理偏好分析
    top_region = max(region_counts.items(), key=lambda x: x[1])
    print(f"5. 最偏好的地理区域: {top_region[0]} ({top_region[1]}条, {top_region[1]/len(data)*100:.1f}%)")
    
    # 特殊发现
    print("\n特殊发现:")
    
    # 统计特殊命名
    special_names = []
    for item in data:
        if any(word in item['地名'] for word in ['江', '河', '山', '湖']):
            special_names.append(item['路名'])
    
    print(f"6. 以自然地理命名的道路: {len(special_names)}条")
    
    # 统计历史文化相关
    historical = []
    for item in data:
        if any(word in item['相关信息'] for word in ['历史', '文化', '古', '旧址']):
            historical.append(item['路名'])
    
    print(f"7. 具有历史文化背景的道路: {len(historical)}条")

def export_analysis_report(data, district_counts, province_counts, region_counts):
    """导出分析报告到文件"""
    report_lines = []
    report_lines.append("# 上海地名道路多维度数据分析报告\n")
    
    # 基础统计
    report_lines.append("## 基础统计")
    report_lines.append(f"- 道路总数：{len(data)}条")
    report_lines.append(f"- 涉及区域：{len(district_counts)}个")
    report_lines.append(f"- 涉及省份：{len(province_counts)}个\n")
    
    # 各区统计
    report_lines.append("## 各区道路数量排名")
    for i, (district, count) in enumerate(district_counts.most_common(), 1):
        report_lines.append(f"{i}. {district}：{count}条")
    report_lines.append("")
    
    # 省份统计
    report_lines.append("## 各省份使用频率排名")
    for i, (province, count) in enumerate(province_counts.most_common(), 1):
        report_lines.append(f"{i}. {province}：{count}次")
    report_lines.append("")
    
    # 地理区域分析
    report_lines.append("## 地理区域分布")
    sorted_regions = sorted(region_counts.items(), key=lambda x: x[1], reverse=True)
    for region, count in sorted_regions:
        percentage = count / len(data) * 100
        report_lines.append(f"- {region}：{count}条 ({percentage:.1f}%)")
    
    # 保存报告
    with open('detailed_analysis_report.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"\n详细分析报告已保存至 detailed_analysis_report.md")

def main():
    """主函数"""
    print("上海地名道路多维度数据分析")
    print("分析开始...")
    
    # 加载数据
    data = load_data()
    
    if not data:
        print("数据加载失败，请检查文件路径")
        return
    
    # 执行各种分析
    district_counts, province_counts = basic_analysis(data)
    region_counts = geographical_analysis(data)
    keyword_analysis(data)
    naming_pattern_analysis(data)
    district_province_correlation(data)
    create_summary_report(data, district_counts, province_counts, region_counts)
    export_analysis_report(data, district_counts, province_counts, region_counts)
    
    print("\n" + "=" * 50)
    print("分析完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()