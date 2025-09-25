The following questions are best practices for an interview
1. fundamentals.py
2.specifictopicwisefundamentals.py
Topics:
1. MRO
2. Inheritence
2.GIL
3. Meta Classes
4. OOP
5. SOLID
6. AsyncIO
7. Multithreading
8. Decorator
Metrics to be noted as per approaches:

functoolwrapper: helps for preserving meta data while calling it to display its tracing class name while adding the decorator.
Debugging: Proper function names in tracebacks/logs.
Introspection: Tools like help(), inspect.signature(), and IDE autocompletion work correctly.
Multiple decorators: Preserves metadata so outer decorators can still see the original function’s name, docstring, and annotations.

cls, self: are naming conventions for PEP-8 standards level of declaration of python supports working with

JWT

 ┌─────────────┐       1. Login Request       ┌──────────────┐
 │   Client    │ ───────────────────────────▶ │ Auth Server  │
 │ (Browser /  │                             │ (Flask, etc.)│
 │  Mobile App)│ ◀─────────────────────────── │              │
 └─────────────┘   2. Return JWT Access Token └──────────────┘
        │
        │ 3. Store Token (Memory / LocalStorage / Cookie)
        │
        │
        │ 4. API Request with Token in Header
        ▼
 ┌─────────────┐      5. Validate Token       ┌──────────────┐
 │   Client    │ ───────────────────────────▶ │ Resource/API │
 │             │                             │ Server       │
 │             │ ◀─────────────────────────── │              │
 └─────────────┘    6. Return Protected Data  └──────────────┘


[ Client ]
    │
    │  POST /login (credentials)
    ▼
[ Auth Service ] ──▶ Create JWT ──▶ Return Token
    │
    │ (Later)
    ▼
[ API Gateway / Microservices ]
    │
    │ Validate JWT (signature, expiry, claims)
    │
    └──▶ Provide Access to Protected Resources

payload = {
    "sub": user.id,
    "name": user.username,
    "role": user.role,
    "iat": now(),
    "exp": now() + timedelta(minutes=15)
}

JSON encode header and payload

Base64URL encode them

Sign using algorithm (HS256 or RS256)

Produces header.payload.signature.
Signing step ensures that no one can tamper with the payload without invalidating the token.

Client stores token (LocalStorage, SessionStorage, HttpOnly Cookie, or Memory).

On every request to a protected route:

Client attaches token in Authorization: Bearer <token> header.

┌──────────────┐
│   Client     │
└──────┬───────┘
       │
       │ 1. Login Request (credentials)
       ▼
┌──────────────┐
│ Auth Service │
│  (Flask)     │
└──────┬───────┘
       │
       │ Verify User
       ▼
┌──────────────┐
│  JWT Builder │
│ (encode+sign)│
└──────┬───────┘
       │
       │ 2. Return Access Token
       ▼
┌──────────────┐
│   Client     │
└──────┬───────┘
       │
       │ 3. Request with Bearer Token
       ▼
┌──────────────┐
│ JWT Middleware│
│ (extract+verify)│
└──────┬───────┘
       │
       │ Verify Signature + Claims
       ▼
  ┌────────────┐       ┌────────────┐
  │ Expired?   │────Yes▶ expired_token_loader()
  │ Valid?     │       │ Return 401 │
  └─────┬──────┘       └────────────┘
        │No
        ▼
┌──────────────┐
│ Protected    │
│ Endpoint     │
└──────────────┘
@jwt.unauthorized_loader When no token is present at all 
@jwt.invalid_token_loader When token is malformed or signature invalid 
@jwt.expired_token_loader When token is valid but expired 
@jwt.needs_fresh_token_loader When token exists but is not "fresh" and fresh required 
@jwt.revoked_token_loader When token is revoked (if you use token revocation/blacklist)

<!-- understand the call flows of any new module introduced along with its architecutre and confirm its utlility in your requiremnts after
having requirements clarity. -->

Client Request → Extract JWT
       │
       ├─ No token? → @unauthorized_loader
       │
       ├─ Invalid signature / malformed? → @invalid_token_loader
       │
       ├─ Expired? → @expired_token_loader
       │
       ├─ Revoked? → @revoked_token_loader
       │
       ├─ Fresh required but not fresh? → @needs_fresh_token_loader
       │
       └─ All good → Proceed to Endpoint


                    ┌────────────────────┐
                    │   Client Request   │
                    └─────────┬──────────┘
                              │
                              ▼
                  ┌─────────────────────┐
                  │ Extract JWT Token   │
                  └─────────┬──────────┘
                            │
             ┌──────────────┴──────────────┐
             │                             │
       Token Present?                   No Token
             │                             │
             ▼                             ▼
  ┌─────────────────────┐        @jwt.unauthorized_loader
  │ Decode & Verify JWT │        (Missing token)
  └─────────┬──────────┘
            │
      Signature Valid?
            │
     ┌──────┴───────┐
     │              │
   Yes              No
     │              │
     ▼              ▼
 Check Expiry     @jwt.invalid_token_loader
     │           (Malformed / Invalid Signature)
     │
  Expired?
     │
 ┌───┴─────┐
 │         │
No         Yes
 │         │
 ▼         ▼
Check Revoked?   @jwt.expired_token_loader
                 (Token expired)
 │
 ┌─┴─┐
 │   │
No   Yes
 │   │
 ▼   ▼
Check Fresh?  @jwt.revoked_token_loader
               (Token revoked)
 │
 ┌─┴─┐
 │   │
Yes  No
 │   │
 ▼   ▼
Proceed to   @jwt.needs_fresh_token_loader
Endpoint     (Fresh token required)
