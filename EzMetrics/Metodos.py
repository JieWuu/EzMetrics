class Metrics:
    '''
    El objetivo de esta clase es calcular metricas de bondad de ajuste para predicciones 
    de modelos de regresion y clasificacion. 
    Esta clase nos devuelve la metrica seleccionada tras recibir una lista con los valores 
    esperados o predichos y una lista con los valores observados o reales.
    Elementos:
        predicted: lista con los valores predichos
        observed: lista con los valores observados
    '''
    def __init__(self, predicted, observed):
        self.predicted=predicted
        self.observed=observed

        observed_values=list(set(self.observed))
        self.positive=observed_values[0]
        self.negative=observed_values[1]

        self.tp_fun=lambda pred,obs: sum([a==self.positive and a==b for a,b in zip(pred,obs)])
        self.tn_fun=lambda pred,obs: sum([a!=self.positive and a==b for a,b in zip(pred,obs)])
        self.fp_fun=lambda pred,obs: sum([a==self.positive and a!=b for a,b in zip(pred,obs)])
        self.fn_fun=lambda pred,obs: sum([a!=self.positive and a!=b for a,b in zip(pred,obs)])

    
    def precission (self,predicted,observed):
        tp=self.tp_fun(predicted,observed)
        fp=self.fp_fun(predicted,observed)
        tp_fp=(tp + fp)
        if not tp_fp:
            tp_fp=0.000001 
        return tp / (tp + fp)

    def recall (self,predicted,observed): # = sensitivity
        tp=self.tp_fun(predicted,observed)
        fn=self.fn_fun(predicted,observed)
        tp_fn=(tp + fn)
        if not tp_fn:
            tp_fn=0.000001 
        return tp / tp_fn

    def specificity (self,predicted,observed):
        tn=self.tn_fun(predicted,observed)
        fp=self.fp_fun(predicted,observed)
        tn_fp=(tn + fp)
        if not tn_fp:
             tn_fp=0.000001
        return tn / tn_fp


    # metricas clasificacion asignada: -------------------------------------
    def accuracy (self):
        tp=self.tp_fun(self.predicted,self.observed)
        tn=self.tn_fun(self.predicted,self.observed)
        return (tp + tn) / len(self.predicted)

    def f1 (self):
        prec=self.precission(self.predicted,self.observed)
        rec=self.recall(self.predicted,self.observed)
        if not (prec + rec):
            prec=0.000001 
        return (2 * (prec * rec) / (prec + rec))


    # metricas clasificacion probabilidad: ---------------------------------
    def roc_auc(self):
        probs=list(set(self.predicted))
        probs+=[0,1]
        probs.sort()

        if len(probs)<=50:
            puntos_corte=[x for x in probs]
        else:
            puntos_corte=[x/100 for x in range(101)]
        
        puntos_curva=[]  
        for i in puntos_corte:
            predicted_0=[self.positive if x >= i else self.negative for x in self.predicted]
            puntos_curva.append([(1-self.specificity(predicted_0,self.observed)),self.recall(predicted_0,self.observed)])

        #grafico y auc
        auc=0
        for i in range(len(puntos_curva)-1):
            area=(puntos_curva[i][1]+puntos_curva[i+1][1])*(puntos_curva[i][0]-puntos_curva[i+1][0])/2
            auc+=area
        
        return auc
        #return (auc,puntos_curva) #esto seria para hacer el grafico


    # metricas regresion: --------------------------------------------------
    def r2(self):
        media=sum(self.observed)/len(self.observed)
        var_pred=[(x-media)**2 for x in self.predicted]
        var_real=[(x-media)**2 for x in self.observed]
        if not sum(var_real):
            var_real=0.000001 
        return 1-(sum(var_pred)/sum(var_real))

    def mae(self):
        error=[abs(a-b) for a,b in zip(self.predicted,self.observed)]
        return (sum(error)/len(self.observed))

    def mse(self):
        error=[(a-b)**2 for a,b in zip(self.predicted,self.observed)]
        return (sum(error)/len(self.observed))
