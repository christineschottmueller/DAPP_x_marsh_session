Policy effects and Thresholds
--------------------------------

This section illustrates how different management strategies—marsh conservation (``fd=0.4``) and marsh restoration (``fd=0.6``)—influence marsh accretion rates over time. Using a fixed set of categorical model inputs, we compare the effects of these strategies under two sea level rise scenarios: RCP2.6 (low emissions) and RCP8.5 (high emissions).

To run the ``marsh_elevation_model`` for the marsh restoration policy, we need to set the variable representing the sediment trapping ability, ``fd``, to 0.6, all other inputs stay fixed for enabling visual comparison of the policy effects. By visualizing these outcomes side by side, we get a better notion of how policy choices shape future marsh development and identify points in time where marsh growth may no longer keep up with rising sea levels—also known as critical thresholds.rise scenarion RCP8.5 and RCP2.6 (X) on marsh accretion rates.


.. code:: ipython3
	
	fd = 0.6                   # Policy: Marsh restoration

    
Now we run the ``marsh_elevation_model```with the changed parameter, store the results in a dictionary and finally unpack it for easier plotting.

.. code:: ipython3

    results = {}

	for result_name, slr_series in slr_series_dict.items():
    merged_data = tides_per_year.merge(slr_series, on='year', how='left')
    #msl_series = merged_data['msl'].values
    
    msl = slr_series['msl']
    z_vals, years, dz_vals = marsh_elevation_model(
        z_init=z_init,
        c_flood=c_flood,
        c_flood_nourishment=c_flood_nourishment,
        fd=fd,
        rho_deposit=rho_deposit,
        s_subsidence=s_subsidence,
        nourishment_frequency=nourishment_frequency,
        tides_per_year=merged_data
    )
     

    results[result_name+ '_restoration'] = pd.DataFrame({
        'year': years,
        'elevation': z_vals,
        'dz_dt': dz_vals,
        'msl': msl,
    })

    # store on disk
	for result_name, df in results.items():
		df.to_csv(f'model_output_M/Accretion_time_series/{result_name}_restoration.txt', sep='\t', index=False)
	
	# unpacking the results dictionary 
	for name, df in results.items():
	   globals()[name] = df		
		

Then we smoothen the elevation change time series with the Savitzky-Golay filter. This step serves purely aesthetic purposes, helping to create cleaner and more visually appealing plots without altering the underlying trends.


.. code:: ipython3

    window_size = 10  # Window size must be odd
	poly_order = 1
	smoothed_low_26_restoration = savgol_filter(result_low_26_restoration['dz_dt'], window_size, poly_order)
	smoothed_mean_26_restoration = savgol_filter(result_mean_26_restoration['dz_dt'], window_size, poly_order)
	smoothed_high_26_restoration = savgol_filter(result_high_26_restoration['dz_dt'], window_size, poly_order)

	smoothed_low_85_restoration = savgol_filter(result_low_85_restoration['dz_dt'], window_size, poly_order)
	smoothed_mean_85_restoration = savgol_filter(result_mean_85_restoration['dz_dt'], window_size, poly_order)
	smoothed_high_85_restoration = savgol_filter(result_high_85_restoration['dz_dt'], window_size, poly_order)
		
    

Plot commands
^^^^^^^^^^^^^^^
Finally, we create one elevation time series for each policy and plot them next to each other for comparison:
 
.. code:: ipython3


	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6), sharey=True)

	### ========== Subplot a) Conservation ==========

	# RCP 2.6
	p1_26_E = ax1.plot(result_mean_26_conservation['year'], result_mean_26_conservation['elevation'],
					   linestyle='--', color='#79BCFF')
	ax1.fill_between(result_mean_26_conservation['year'], result_low_26_conservation['elevation'],
					 result_high_26_conservation['elevation'], color='#DDA63A', alpha=0.4)

	p1_26_slr = ax1.plot(result_mean_26_conservation['year'], result_mean_26_conservation['msl'],
						 linestyle='-', color='#79BCFF', linewidth=2)
	ax1.fill_between(result_low_26_conservation['year'], result_low_26_conservation['msl'],
					 result_high_26_conservation['msl'], color='#79BCFF', alpha=0.2)

	# RCP 8.5
	p1_85_E = ax1.plot(result_mean_85_conservation['year'], result_mean_85_conservation['elevation'],
					   linestyle='--', color='#FF0000')
	ax1.fill_between(result_low_85_conservation['year'], result_low_85_conservation['elevation'],
					 result_high_85_conservation['elevation'], color='#8C6518', alpha=0.4)

	p1_85_slr = ax1.plot(result_mean_85_conservation['year'], result_mean_85_conservation['msl'],
						 linestyle='-', color='#FF0000', linewidth=2)
	ax1.fill_between(result_low_85_conservation['year'], result_low_85_conservation['msl'],
					 result_high_85_conservation['msl'], color='#FF0000', alpha=0.2)

	# Dummy handles for legend
	p2_26_E = ax1.fill(np.NaN, np.NaN, color='#DDA63A', alpha=0.4)
	p2_85_E = ax1.fill(np.NaN, np.NaN, color='#8C6518', alpha=0.4)
	p2_26_slr = ax1.fill(np.NaN, np.NaN, color='#79BCFF', alpha=0.2)
	p2_85_slr = ax1.fill(np.NaN, np.NaN, color='#FF0000', alpha=0.4)

	handles1 = [(p1_26_slr[0], p2_26_slr[0]), (p1_85_slr[0], p2_85_slr[0]),
				(p1_26_E[0], p2_26_E[0]), (p1_85_E[0], p2_85_E[0])]
	labels1 = [r'Sea level $_{RCP 2.6}$', r'Sea level $_{RCP 8.5}$',
			   r'Elevation $_{RCP 2.6}$, conservation',
			   r'Elevation $_{RCP 8.5}$, conservation']

	ax1.legend(handles1, labels1, ncol=2, handleheight=1, prop={'size': 13},
			   loc='upper left', frameon=False)
	ax1.set_title("a) Conservation", loc='left', fontsize=14)
	ax1.set_ylabel('[meter]')
	ax1.set_xlim(2044, 2100)
	ax1.set_ylim(0.17, 1.2)
	ax1.grid(True)
	ax1.grid(axis='x', visible=False)


	### ========== Subplot b) Restoration ==========

	# RCP 2.6
	p1_26_E = ax2.plot(result_mean_26_restoration['year'], result_mean_26_restoration['elevation'],
					   linestyle='--', color='#79BCFF')
	ax2.fill_between(result_low_26_restoration['year'], result_low_26_restoration['elevation'],
					 result_high_26_restoration['elevation'], color='#8FC36B', alpha=0.5)

	p1_26_slr = ax2.plot(result_mean_26_restoration['year'], result_mean_26_restoration['msl'],
						 linestyle='-', color='#79BCFF', linewidth=2)
	ax2.fill_between(result_low_26_restoration['year'], result_low_26_restoration['msl'],
					 result_high_26_restoration['msl'], color='#79BCFF', alpha=0.2)

	# RCP 8.5
	p1_85_E = ax2.plot(result_mean_85_restoration['year'], result_mean_85_restoration['elevation'],
					   linestyle='--', color='#FF0000')
	ax2.fill_between(result_low_85_restoration['year'], result_low_85_restoration['elevation'],
					 result_high_85_restoration['elevation'], color='#3F7E44', alpha=0.5)

	p1_85_slr = ax2.plot(result_mean_85_restoration['year'], result_mean_85_restoration['msl'],
						 linestyle='-', color='#FF0000', linewidth=2)
	ax2.fill_between(result_low_85_restoration['year'], result_low_85_restoration['msl'],
					 result_high_85_restoration['msl'], color='#FF0000', alpha=0.2)

	# Dummy handles for legend
	p2_26_E = ax2.fill(np.NaN, np.NaN, color='#8FC36B', alpha=0.4)
	p2_85_E = ax2.fill(np.NaN, np.NaN, color='#3F7E44', alpha=0.4)
	p2_26_slr = ax2.fill(np.NaN, np.NaN, color='#79BCFF', alpha=0.2)
	p2_85_slr = ax2.fill(np.NaN, np.NaN, color='#FF0000', alpha=0.3)

	handles2 = [(p1_26_slr[0], p2_26_slr[0]), (p1_85_slr[0], p2_85_slr[0]),
				(p1_26_E[0], p2_26_E[0]), (p1_85_E[0], p2_85_E[0])]
	labels2 = [r'Sea level $_{RCP 2.6}$', r'Sea level $_{RCP 8.5}$',
			   r'Elevation $_{RCP 2.6}$, restoration',
			   r'Elevation $_{RCP 8.5}$, restoration']

	ax2.legend(handles2, labels2, ncol=2, handleheight=1, prop={'size': 13},
			   loc='upper left', frameon=False)
	ax2.set_title("b) Restoration", loc='left', fontsize=14)
	ax2.set_xlim(2044, 2100)
	ax2.grid(True)
	ax2.grid(axis='x', visible=False)

	# Shared style
	sns.set_context("talk", font_scale=0.7)
	plt.tight_layout()
	plt.savefig('elevation_ts_S15_combined.png', dpi=300)
	plt.show()


  
   
.. figure:: img/elevation_ts_S15_combined.png.png
   :alt: Comparison of the effects two management policies on marsh elevation change the pioneer zone in focus area 15.
   :width: 500px
   :align: center

   Comparison of the effects of two management policies on marsh elevation change the pioneer zone in focus area 15. 
   The simulations were performed using water level inputs from the high and low emissions scenarios RCP 2.6 and RCP8.5 (X).

  