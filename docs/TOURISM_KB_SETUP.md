# Tourism Guide AI - Knowledge Base Setup Guide

## Overview

This guide explains how to populate the Tourism Guide AI knowledge base with tourism information. The chatbot uses RAG (Retrieval-Augmented Generation) to provide accurate, sourced information about tourist destinations.

## Knowledge Base Structure

### File Format
- Use Markdown (.md) files for easy parsing and formatting
- One file per major destination or region
- Clear section headers for organized information

### Recommended File Organization

```
docs/
├── destinations/
│   ├── asia/
│   │   ├── india/
│   │   │   ├── taj-mahal.md
│   │   │   ├── delhi.md
│   │   │   └── agra.md
│   │   ├── thailand/
│   │   │   ├── bangkok.md
│   │   │   └── phuket.md
│   ├── europe/
│   │   ├── france/
│   │   │   └── paris.md
│   ├── americas/
│   └── africa/
├── guides/
│   ├── travel-tips.md
│   ├── budget-travel.md
│   ├── family-travel.md
│   └── adventure-travel.md
└── reference/
    ├── transport-options.md
    └── visa-information.md
```

## Document Template

Use this template for creating tourism documents:

```markdown
# [Destination Name]

## Quick Facts
- **Location**: [Complete address and GPS coordinates]
- **Region**: [State/Province/Country]
- **Distance from**: [Major reference cities with km]
- **Time Zone**: [UTC offset]
- **Language**: [Primary languages spoken]

## Historical & Cultural Significance

[2-3 paragraphs about the historical importance, cultural significance, heritage status, and major historical events]

## Top Attractions

### Primary Attractions
1. **[Attraction Name]**
   - Description and significance
   - Entry fee: [Amount]
   - Timings: [Hours]
   - Time needed: [Duration]

2. **[Attraction Name]**
   - [Details...]

### Secondary Attractions
- [List nearby attractions]

## Practical Information

### Entry & Access
- **Main Entry Fee**: [Amount with any discounts]
- **Photography Fee**: [If applicable]
- **Opening Hours**: [Days and timings]
- **Best Time to Visit**: [Seasons and reasons]
- **Accessibility**: [Wheelchair access, facilities, etc.]

### Visiting Duration
- Quick visit: [X hours/days]
- Recommended visit: [X hours/days]
- Complete experience: [X hours/days]

## Best Times to Visit

### By Season
- **Summer** (Jun-Aug): [Weather, crowds, pros/cons]
- **Monsoon** (Sep-Oct): [Weather, crowds, pros/cons]
- **Autumn** (Nov-Dec): [Weather, crowds, pros/cons]
- **Winter** (Jan-Mar): [Weather, crowds, pros/cons]

### Crowd Levels
- **Peak Season**: [Months with high tourism]
- **Off-Season**: [Quieter months]
- **Sweet Spot**: [Best time with balance of weather and crowds]

## Getting There

### From Major Cities
- **From [City Name]**: 
  - Distance: [X km]
  - By Bus: [Duration, frequency, cost]
  - By Train: [Duration, frequency, cost]
  - By Flight: [Duration, cost]
  - By Car/Cab: [Duration, rental cost]

### Local Transportation
- [Taxi/Auto options]
- [Public transport]
- [Rental options]

## Accommodation Options

### Luxury
- [Hotel recommendations with ratings and price range]

### Mid-Range
- [Recommendations]

### Budget
- [Recommendations]
- [Hostels if available]

## Dining & Local Specialties

### Must-Try Dishes
1. **[Dish Name]**: [Description and where to try]
2. **[Dish Name]**: [Description]

### Recommended Restaurants
- [Restaurant names with cuisine types]

### Street Food & Local Markets
- [Popular street food items]
- [Market locations]

## Activities & Experiences

- [Adventure activities]
- [Cultural experiences]
- [Spiritual activities]
- [Photography opportunities]
- [Shopping areas]

## What Makes It Special

[2-3 paragraphs explaining the unique characteristics, why this destination is worth visiting, what makes it different from similar places]

## Nearby Attractions

### Within 10-50 km
- [Nearby destination with distance and significance]

### Within 50-100 km
- [Nearby destination]

## Travel Tips

- [Safety information]
- [What to carry]
- [Cultural etiquette]
- [Money and payment]
- [Communication (SIM cards, WiFi)]
- [Best places to stay]
- [Pickpocketing and safety]
- [Guided tours vs solo]

## Special Considerations

### For Families
- [Family-friendly activities]
- [Child facilities]
- [Safety for children]

### For Solo Travelers
- [Safe areas and neighborhoods]
- [Social gathering spots]
- [Budget tips]

### For Adventure Seekers
- [Adventure activities available]
- [Safety precautions]
- [Fitness requirements]

### For Budget Travelers
- [Cheap accommodation]
- [Affordable food options]
- [Free or low-cost attractions]

## Contact Information

- **Tourist Information Center**: [Address and phone]
- **Local Tourism Board**: [Website]
- **Emergency Services**: [Phone numbers]

## Related Destinations

- [Link to nearby major attractions]
- [Popular combination itineraries]

## References & Sources

- [Official tourism website]
- [Travel guides]
- [Recent travel blogs/articles]
- [Date of last update]

---

**Last Updated**: [Date]
**Verified By**: [Name/Source]
```

## Content Guidelines

### Writing Style
✅ DO:
- Use clear, descriptive language
- Include specific details (prices, hours, distances)
- Use friendly, engaging tone
- Provide practical information
- Be accurate and up-to-date

❌ DON'T:
- Use overly technical language
- Make unverified claims
- Copy entire content from other sources without attribution
- Provide outdated information
- Use misleading information

### Information Accuracy
- Verify all facts before including
- Include sources for statistics
- Update regularly (at least annually)
- Note any seasonal variations
- Mention if information is subject to change

### Pricing & Costs
- Always indicate currency
- Include discounts for children, seniors, students
- Mention if free entry for certain categories
- Update regularly as prices change
- Note any package deals

### Timing Information
- Provide operating hours with days
- Mention seasonal variations in hours
- Include time needed for each activity
- Account for travel time between attractions

## Uploading to Knowledge Base

1. **Using the Web Interface**:
   - Login to Tourism Guide AI
   - Go to Documents section
   - Upload markdown files
   - System will process and index content

2. **Using Document Upload API**:
   ```python
   from frontend.services import uploadDocument
   
   with open('taj-mahal.md', 'rb') as f:
       await uploadDocument(f)
   ```

3. **Direct File Management**:
   - Place files in `docs/` directory
   - Run indexing command
   - Restart chatbot service

## Quality Checklist

Before uploading content, verify:

- [ ] All information is accurate and current
- [ ] Contact information is valid
- [ ] Prices and fees are up-to-date
- [ ] Opening hours are correct
- [ ] Geographic locations are precise
- [ ] No spelling or grammar errors
- [ ] Formatting is consistent
- [ ] All sections are complete
- [ ] Sources are cited
- [ ] Content is original or properly attributed

## Examples

### Example 1: Historical Monument
```markdown
# Taj Mahal, Agra

## Quick Facts
- **Location**: Dharmapuri, Forest Colony, Tajganj, Agra, Uttar Pradesh 282001, India
- **GPS**: 27.1751° N, 78.0421° E
- **Region**: Uttar Pradesh, India
- **Built**: 1632-1653
...
```

### Example 2: Natural Destination
```markdown
# Kerala Backwaters

## Quick Facts
- **Location**: Multiple locations across Kottayam and Alappuzha districts, Kerala
...
```

## Maintenance

### Regular Updates
- Monthly: Verify prices and hours
- Quarterly: Update travel conditions and tips
- Annually: Comprehensive review and refresh

### Version Control
- Track changes to documents
- Maintain update logs
- Archive outdated versions

---

**Version**: 1.0
**Last Updated**: May 28, 2026
