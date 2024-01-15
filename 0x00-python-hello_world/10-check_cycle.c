#include "lists.h"

/**
 * check_cycle - function that checks a singly linked list has a cycle in it
 * @list: a pointer to the struct listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *next = list, *aft = list;

	if (!list)
		return (0);
	while (next && aft && aft->next)
	{
		next = next->next;
		aft = aft->next->next;
		if (next == aft)
		{
			return (1);
		}
	}
	return (0);
}
