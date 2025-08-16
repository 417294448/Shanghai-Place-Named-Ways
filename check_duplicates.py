#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查重复道路和数据统计
"""

from collections import Counter

def load_and_check_data():
    """加载数据并检查重复"""
    data = []
    file_path = '/Users/xiaoshuang/Documents/cursor_code/Shanghai-Place-Named-Ways/by_district/all.md'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 解析表格数据
    lines = content.split('\n')
    total_lines = 0
    
    for line in lines:
        if line.startswith('|') and '区域' not in line and '---' not in line and len(line.strip()) > 5:
            total_lines += 1
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 4:
                data.append({
                    '区域': parts[0],
                    '路名': parts[1], 
                    '省份': parts[2],
                    '地名': parts[3]
                })
    
    print(f"原始数据行数: {total_lines}")
    print(f"有效数据条数: {len(data)}")
    
    # 检查重复道路
    road_names = [item['路名'] for item in data]
    road_counter = Counter(road_names)
    duplicates = {road: count for road, count in road_counter.items() if count > 1}
    
    print(f"\n重复道路统计:")
    print(f"重复道路数量: {len(duplicates)}")
    print(f"重复条目总数: {sum(duplicates.values()) - len(duplicates)}")
    
    if duplicates:
        print("\n具体重复道路:")
        for road, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
            print(f"  {road}: {count}次")
            # 显示重复道路的详细信息
            for item in data:
                if item['路名'] == road:
                    print(f"    - {item['区域']} | {item['省份']} | {item['地名']}")
    
    # 去重后统计
    unique_roads = set(road_names)
    print(f"\n去重后道路总数: {len(unique_roads)}")
    
    # 重新统计各区和省份
    unique_data = []
    seen_roads = set()
    for item in data:
        if item['路名'] not in seen_roads:
            unique_data.append(item)
            seen_roads.add(item['路名'])
    
    print(f"\n去重后统计:")
    district_counts = Counter([item['区域'] for item in unique_data])
    province_counts = Counter([item['省份'] for item in unique_data])
    
    print(f"涉及区域: {len(district_counts)}个")
    print(f"涉及省份: {len(province_counts)}个")
    
    print("\n各区道路数量(去重后):")
    for district, count in district_counts.most_common():
        print(f"  {district}: {count}条")
    
    print("\n各省份使用频率(去重后):")
    for province, count in province_counts.most_common(15):
        print(f"  {province}: {count}次")

if __name__ == "__main__":
    load_and_check_data()