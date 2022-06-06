[14:07] Ying Xu
IHC_li = clip(IHC_li_l[:,4000:], 0, amax(IHC_li_l[:,4000:]))


tau_LIF = 10 * 1e-3
c_LIF = 1 / (fs * tau_LIF)


LIF = zeros((nsec, npoints))
spk = zeros((nsec, npoints))

thres = 0.00004



V_reset = -0.001
for s in range(nsec):
    for t in range(npoints):


        LIF[s, t] = LIF[s, t - 1] + c_LIF * (IHC_li[s, t] - LIF[s, t - 1])




        if LIF[s, t] > thres:
            spk[s, t] = 1
            LIF[s, t] = V_reset
        else:
            spk[s, t] = 0


