package com.devops.auth;

import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
public class AuthController {

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "UP");
    }

    @GetMapping("/ready")
    public Map<String, Boolean> ready() {
        return Map.of("ready", true);
    }

    @PostMapping("/authenticate")
    public Map<String, Object> authenticate() {

        return Map.of(
                "authenticated", true,
                "user", "demo-user",
                "roles", new String[]{"USER"}
        );
    }
}