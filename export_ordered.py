import json
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
各区道路清单列表信息生成，用于前端展示
"""

def export_ordered_roads():
    with open('/Users/xiaoshuang/Documents/cursor_code/Shanghai-Place-Named-Ways/by_district/all.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    roads = []
    for line in content.split('\n'):
        if line.startswith('|') and '区域' not in line and '---' not in line and len(line.strip()) > 5:
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 5:
                roads.append({
                    'district': parts[0],
                    'road': parts[1],
                    'province': parts[2],
                    'info': parts[4]
                })
    
    order = ["杨浦区", "虹口区", "静安区", "宝山区", "闵行区", "普陀区", "浦东新区", "长宁区", "黄浦区", "徐汇区", "嘉定区", "崇明区", "奉贤区", "松江区", "金山区", "青浦区"]
    
    ordered_roads = []
    for district in order:
        for road in roads:
            if road['district'] == district:
                ordered_roads.append(road)
    
    print('[')
    for i, road in enumerate(ordered_roads):
        comma = ',' if i < len(ordered_roads) - 1 else ''
        print(f'  {{\n    district: "{road["district"]}",\n    road: "{road["road"]}",\n    province: "{road["province"]}",\n    info: "{road["info"]}",\n  }}{comma}')
    print(']')

if __name__ == "__main__":
    export_ordered_roads()