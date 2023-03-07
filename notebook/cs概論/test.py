import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(294/25.4, 210/25.4))
ax = fig.add_axes([0.10, 0.10, 0.80, 0.80], projection=ccrs.PlateCarree())
# ---
# 別の図法で描きたい場合は例えば以下のようにする。
# たくさんの図法が用意されています。
# ax = fig.add_axes([0.10, 0.10, 0.80, 0.80], projection=ccrs.Mercator())
# ax = fig.add_axes([0.10, 0.10, 0.80, 0.80], projection=ccrs.Robinson())
# ax = fig.add_axes([0.10, 0.10, 0.80, 0.80], projection=ccrs.LambertCylindrical())
# ax = fig.add_axes([0.10, 0.10, 0.80, 0.80], projection=ccrs.LambertConformal())

ax.set_extent([120, 160, 20, 50], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES)
ax.add_feature(cfeature.RIVERS)

# --- 通天閣の位置
ax.scatter(135+30/60+22.77/60/60, 34.0+39/60 +
           9.13/60/60, transform=ccrs.PlateCarree())

# --- 緯線と経線
ax.gridlines(linestyle='dashed', color='gray',
             linewidth=0.5,  draw_labels=True)

plt.savefig('map-japan.png')

