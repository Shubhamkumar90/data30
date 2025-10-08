import matplotlib.pyplot as plt
months=['jan','feb','mar','apr','may','jun']
sales=[200,300,500,100,350,200]
# plt.plot(months,sales,marker='o',color='pink', linestyle='dashdot')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.show()
fig,ax=plt.subplots(1,2,figsize=(10,4),facecolor='lightgrey')

ax[0].set_facecolor('#ffe4b5')
ax[0].plot(months, sales, marker='o', color='green')
ax[0].set_title('Sales Over Months')
ax[0].set_xlabel('Month')
ax[0].set_ylabel('Sales')

ax[1].set_facecolor('lavender')
ax[1].bar(months, sales, color='orange')
ax[1].set_title('Sales Bar Chart')
ax[1].set_xlabel('Month')
ax[1].set_ylabel('Sales')

plt.tight_layout()
plt.show()
