package com.ecdat.test;

public class PaymentProcessor {

    private CryptoHelper cryptoHelper;

    public PaymentProcessor() {
        this.cryptoHelper = new CryptoHelper();
    }

    public String processPayment(String cardNumber, double amount) throws Exception {
        byte[] encryptedCard = CryptoHelper.encryptDES(cardNumber.getBytes());
        return "PAYMENT_" + encryptedCard.length + "_" + amount;
    }
}
