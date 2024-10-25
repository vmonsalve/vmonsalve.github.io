---
layout: post
title: Dotnet entity framework first code
---

# Dotnet entity framework first code

```csharp
namespace API.Entities;

public class AppUser
{
    public int Id { get; set; }
    public required string UserName { get; set; }
    public required byte[] PasswordHash { get; set; }
    public required byte[] PasswordSalt { get; set; }
}
```
