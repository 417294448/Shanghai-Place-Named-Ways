# 上海地名道路多维度数据分析报告

## 基础统计
- 道路总数：872条
- 涉及区域：16个
- 涉及省份：36个

## 各区道路数量排名
1. 黄浦区：124条
2. 杨浦区：100条
3. 虹口区：95条
4. 徐汇区：94条
5. 静安区：91条
6. 普陀区：64条
7. 长宁区：62条
8. 宝山区：53条
9. 闵行区：51条
10. 浦东新区：45条
11. 嘉定区：30条
12. 崇明区：20条
13. 松江区：20条
14. 奉贤区：14条
15. 金山区：5条
16. 青浦区：4条

## 各省份使用频率排名
1. 浙江：60次
2. 江苏：57次
3. 四川：55次
4. 陕西：54次
5. 云南：51次
6. 新疆：49次
7. 广西：49次
8. 山东：43次
9. 广东：41次
10. 山西：39次
11. 河北：37次
12. 甘肃：35次
13. 黑龙江：35次
14. 辽宁：29次
15. 贵州：27次
16. 吉林：25次
17. 湖南：24次
18. 江西：21次
19. 内蒙古：19次
20. 福建：18次
21. 河南：17次
22. 湖北：16次
23. 安徽：14次
24. 北京：15次
25. 台湾：8次
26. 重庆：8次
27. 西藏：7次
28. 天津：5次
29. 海南：4次
30. 香港：3次
31. 宁夏：3次
32. 青海：2次
35. 上海：1次
36. 澳门：1次

## 地理区域分布
- 华东：213条 (24.4%)
- 西北：143条 (16.4%)
- 西南：140条 (16.1%)
- 华北：112条 (12.8%)
- 华南：94条 (10.8%)
- 东北：89条 (10.2%)
- 华中：57条 (6.5%)
- 港澳台：12条 (1.4%)



// 摘要统计（来自文档）
export const countsByDistrict: { name: string; value: number }[] = [
  { name: "黄浦区", value: 124 },
  { name: "杨浦区", value: 100 },
  { name: "虹口区", value: 95 },
  { name: "徐汇区", value: 94 },
  { name: "静安区", value: 91 },
  { name: "普陀区", value: 64 },
  { name: "长宁区", value: 62 },
  { name: "宝山区", value: 53 },
  { name: "闵行区", value: 51 },
  { name: "浦东新区", value: 45 },
  { name: "嘉定区", value: 30 },
  { name: "崇明区", value: 20 },
  { name: "松江区", value: 20 },
  { name: "奉贤区", value: 14 },
  { name: "金山区", value: 5 },
  { name: "青浦区", value: 4 },
]

export const freqByProvince: { name: string; value: number }[] = [
  { name: "浙江", value: 60 },
  { name: "江苏", value: 57 },
  { name: "四川", value: 55 },
  { name: "陕西", value: 54 },
  { name: "云南", value: 51 },
  { name: "新疆", value: 49 },
  { name: "广西", value: 49 },
  { name: "山东", value: 43 },
  { name: "广东", value: 41 },
  { name: "山西", value: 39 },
  { name: "河北", value: 37 },
  { name: "甘肃", value: 35 },
  { name: "黑龙江", value: 35 },
  { name: "辽宁", value: 29 },
  { name: "贵州", value: 27 },
  { name: "吉林", value: 25 },
  { name: "湖南", value: 24 },
  { name: "江西", value: 21 },
  { name: "内蒙古", value: 19 },
  { name: "福建", value: 18 },
  { name: "河南", value: 17 },
  { name: "湖北", value: 16 },
  { name: "安徽", value: 14 },
  { name: "北京", value: 15 },
  { name: "台湾", value: 8 },
  { name: "重庆", value: 8 },
  { name: "西藏", value: 7 },
  { name: "天津", value: 5 },
  { name: "海南", value: 4 },
  { name: "香港", value: 3 },
  { name: "宁夏", value: 3 },
  { name: "青海", value: 2 },
  { name: "上海", value: 1 },
  { name: "澳门", value: 1 }
]

// “相关信息”关键词统计（未变更）
export const keywordCounts: { name: string; value: number }[] = [
  { name: "社区商业", value: 21 },
  { name: "商圈", value: 15 },
  { name: "美食/餐饮", value: 14 },
  { name: "工业", value: 6 },
  { name: "公园", value: 5 },
  { name: "学校/大学", value: 4 },
]

// 一些衍生统计
export const totalRoads = 872
export const districtCount = 16
export const provinceCount = 36

// 添加地理分布数据
export const geographicDistribution: { name: string; value: number; percentage: string }[] = [
  { name: "华东", value: 213, percentage: "24.4%" },
  { name: "西北", value: 143, percentage: "16.4%" },
  { name: "西南", value: 140, percentage: "16.1%" },
  { name: "华北", value: 112, percentage: "12.8%" },
  { name: "华南", value: 94, percentage: "10.8%" },
  { name: "东北", value: 89, percentage: "10.2%" },
  { name: "华中", value: 57, percentage: "6.5%" },
  { name: "港澳台", value: 12, percentage: "1.4%" },
]