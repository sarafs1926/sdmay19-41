from migen import *

"""
Top level spectrometer application module.
"""
class spectrometer_top(Module):
    def __init__(self, adc, tengbe, reg, clk):
        self.specials += Instance("spectrometer_app"
            spectrometer_app_adc_user_data_i0 = adc.data_i0,
            spectrometer_app_adc_user_data_i1 = adc.data_i1,
            spectrometer_app_adc_user_data_i2 = adc.data_i2,
            spectrometer_app_adc_user_data_i3 = adc.data_i3,
            spectrometer_app_adc_user_data_i4 = adc.data_i4,
            spectrometer_app_adc_user_data_i5 = adc.data_i5,
            spectrometer_app_adc_user_data_i6 = adc.data_i6,
            spectrometer_app_adc_user_data_i7 = adc.data_i7,
            spectrometer_app_adc_user_data_q0 = adc.data_q0,
            spectrometer_app_adc_user_data_q1 = adc.data_q1,
            spectrometer_app_adc_user_data_q2 = adc.data_q2,
            spectrometer_app_adc_user_data_q3 = adc.data_q3,
            spectrometer_app_adc_user_data_q4 = adc.data_q4,
            spectrometer_app_adc_user_data_q5 = adc.data_q5,
            spectrometer_app_adc_user_data_q6 = adc.data_q6,
            spectrometer_app_adc_user_data_q7 = adc.data_q7,
            spectrometer_app_adc_sync = adc.sync,
            spectrometer_app_fft_shift_user_data_out = reg.fft_shift_user_data_out,
            spectrometer_app_ss_adc_bram_data_out = reg.ss_adc_bram_data_out,
            spectrometer_app_ss_adc_ctrl_user_data_out = reg.ss_adc_ctrl_user_data_out,
            spectrometer_app_sync_arm_user_data_out = reg.sync_arm_user_data_out,
            spectrometer_app_sync_sync_time_user_data_out = reg.sync_sync_time_user_data_out,
            spectrometer_app_tge_core_led_rx = tengbe.led_rx,
            spectrometer_app_tge_core_led_tx = tengbe.led_tx,
            spectrometer_app_tge_core_led_up = tengbe.led_up,
            spectrometer_app_tge_core_rx_bad_frame = tengbe.rx_bad_frame,
            spectrometer_app_tge_core_rx_data = tengbe.rx_data,
            spectrometer_app_tge_core_rx_end_of_frame = tengbe.rx_end_of_frame,
            spectrometer_app_tge_core_rx_overrun = tengbe.rx_overrun,
            spectrometer_app_tge_core_rx_source_ip = tengbe.rx_source_ip,
            spectrometer_app_tge_core_rx_source_port = tengbe.rx_source_port,
            spectrometer_app_tge_core_rx_valid = tengbe.rx_valid,
            spectrometer_app_tge_core_tx_afull = tengbe.tx_afull,
            spectrometer_app_tge_core_tx_overflow = tengbe.tx_overflow,
            spectrometer_app_tge_core_txs_ss_bram_data_out = tengbe.txs_ss_bram_data_out,
            spectrometer_app_tge_core_txs_ss_ctrl_user_data_out = tengbe.txs_ss_ctrl_user_data_out,
            spectrometer_app_tge_ctr_rst_user_data_out = reg.tge_ctr_rst_user_data_out,
            spectrometer_app_tge_dest_ip_user_data_out = reg.tge_dest_ip_user_data_out,
            spectrometer_app_tge_dest_port_user_data_out = reg.tge_dest_port_user_data_out,
            spectrometer_app_tge_en_user_data_out = reg.tge_en_user_data_out,
            spectrometer_app_tge_rst_user_data_out = reg.tge_rst_user_data_out,
            spectrometer_app_timebase_sync_period_user_data_out = reg.timebase_sync_period_user_data_out,
            spectrometer_app_tvg_en_user_data_out = reg.tvg_en_user_data_out,
            spectrometer_app_vacc_ss_sel_user_data_out = reg.vacc_ss_sel_user_data_out,
            spectrometer_app_vacc_ss_ss_bram_data_out = reg.vacc_ss_ss_bram_data_out,
            spectrometer_app_vacc_ss_ss_ctrl_user_data_out = reg.vacc_ss_ss_ctrl_user_data_out,
            clk = clk,
            spectrometer_app_crosspower_vacc_of_count_user_data_in = reg.crosspower_vacc_of_count_user_data_in,
            spectrometer_app_fft_of_user_data_in = reg.fft_of_user_data_in,
            spectrometer_app_led0_gateway = reg.led0_gateway,
            spectrometer_app_led1_gateway = reg.led1_gateway,
            spectrometer_app_led2_gateway = reg.led2_gateway,
            spectrometer_app_led3_gateway = reg.led3_gateway,
            spectrometer_app_power_vacc0_of_count_user_data_in = reg.power_vacc0_of_count_user_data_in,
            spectrometer_app_power_vacc1_of_count_user_data_in = reg.power_vacc1_of_count_user_data_in,
            spectrometer_app_ss_adc_bram_addr = reg.ss_adc_bram_addr,
            spectrometer_app_ss_adc_bram_data_in = reg.ss_adc_bram_data_in,
            spectrometer_app_ss_adc_bram_we = reg.ss_adc_bram_we,
            spectrometer_app_ss_adc_status_user_data_in = reg.ss_adc_status_user_data_in,
            spectrometer_app_sync_count_user_data_in = reg.sync_count_user_data_in,
            spectrometer_app_sync_period_user_data_in = reg.sync_period_user_data_in,
            spectrometer_app_sync_uptime_user_data_in = reg.sync_uptime_user_data_in,
            spectrometer_app_tge_core_rst = tengbe.rst,
            spectrometer_app_tge_core_rx_ack = tengbe.rx_ack,
            spectrometer_app_tge_core_rx_overrun_ack = tengbe.rx_overrun_ack,
            spectrometer_app_tge_core_tx_data = tengbe.tx_data,
            spectrometer_app_tge_core_tx_dest_ip = tengbe.tx_dest_ip,
            spectrometer_app_tge_core_tx_dest_port = tengbe.tx_dest_port,
            spectrometer_app_tge_core_tx_end_of_frame = tengbe.tx_end_of_frame,
            spectrometer_app_tge_core_tx_valid = tengbe.tx_valid,
            spectrometer_app_tge_core_txctr_user_data_in = tengbe.txctr_user_data_in,
            spectrometer_app_tge_core_txerrctr_user_data_in = tengbe.txerrctr_user_data_in,
            spectrometer_app_tge_core_txfullctr_user_data_in = tengbe.txfullctr_user_data_in,
            spectrometer_app_tge_core_txofctr_user_data_in = tengbe.txofctr_user_data_in,
            spectrometer_app_tge_core_txs_ss_bram_addr = tengbe.txs_ss_bram_addr,
            spectrometer_app_tge_core_txs_ss_bram_data_in = tengbe.txs_ss_bram_data_in,
            spectrometer_app_tge_core_txs_ss_bram_we = tengbe.txs_ss_bram_we,
            spectrometer_app_tge_core_txs_ss_status_user_data_in = tengbe.txs_ss_status_user_data_in,
            spectrometer_app_tge_core_txvldctr_user_data_in = tengbe.txvldctr_user_data_in,
            spectrometer_app_vacc_output_acc_cnt_user_data_in = reg.vacc_output_acc_cnt_user_data_in,
            spectrometer_app_vacc_ss_ss_bram_addr = reg.vacc_ss_ss_bram_addr,
            spectrometer_app_vacc_ss_ss_bram_data_in = reg.vacc_ss_ss_bram_data_in,
            spectrometer_app_vacc_ss_ss_bram_we = reg.vacc_ss_ss_bram_we,
            spectrometer_app_vacc_ss_ss_status_user_data_in = reg.vacc_ss_ss_status_user_data_in
        )