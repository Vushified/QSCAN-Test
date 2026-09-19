package com.ecdat.test;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.MessageDigest;

/**
 * ECDAT E2E Test — Intentionally vulnerable crypto
 * DO NOT USE IN PRODUCTION
 */
public class CryptoHelper {

    private static final byte[] DES_KEY = "8bytkey!".getBytes();

    public static byte[] encryptDES(byte[] data) throws Exception {
        // VULNERABLE: DES is broken classically (56-bit key, 1998)
        SecretKeySpec keySpec = new SecretKeySpec(DES_KEY, "DES");
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, keySpec);
        return cipher.doFinal(data);
    }

    public static String hashMD5(String input) throws Exception {
        // VULNERABLE: MD5 broken since 2004
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hash = md.digest(input.getBytes("UTF-8"));
        StringBuilder sb = new StringBuilder();
        for (byte b : hash) sb.append(String.format("%02x", b));
        return sb.toString();
    }
}
