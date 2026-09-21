package com.ecdat.test;

import java.security.*;

public class UserAuth {

    public static String generateToken(String userId) throws Exception {
        // VULNERABLE: SHA-1 broken (SHAttered 2017)
        MessageDigest sha = MessageDigest.getInstance("SHA-1");
        byte[] hash = sha.digest(userId.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b : hash) sb.append(String.format("%02x", b));
        return sb.toString();
    }

    public static KeyPair generateRSAKeys() throws Exception {
        // VULNERABLE: RSA-2048 broken by Shor's algorithm
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        return kpg.generateKeyPair();
    }
}
